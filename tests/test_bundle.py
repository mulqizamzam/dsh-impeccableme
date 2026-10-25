from __future__ import annotations
import re, stat, subprocess, tempfile, unittest
import json
from pathlib import Path
from zipfile import ZipFile

ROOT=Path(__file__).resolve().parents[1]
SKILLS=ROOT/".dsh"/"skills"
SLUG=re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

def metadata(path: Path):
    text=path.read_text(encoding="utf-8")
    if not text.startswith("---\n"): raise AssertionError(f"missing frontmatter: {path}")
    end=text.find("\n---\n",4)
    if end<0: raise AssertionError(f"missing closing frontmatter: {path}")
    values={}
    for line in text[4:end].splitlines():
        key,sep,value=line.partition(":")
        if sep and key.strip() and value.strip():
            values[key.strip()]=value.strip().strip("\"'")
    return values,text[end+5:]

class BundleTests(unittest.TestCase):
    def test_exactly_eight_direct_skill_directories(self):
        dirs=sorted(SKILLS.iterdir())
        self.assertEqual(len(dirs),8)
        for item in dirs:
            self.assertTrue(item.is_dir(),item)
            self.assertTrue((item/"SKILL.md").is_file(),item)
            self.assertRegex(item.name,SLUG)

    def test_skill_metadata_matches_directory(self):
        names=set()
        for path in sorted(SKILLS.glob("*/SKILL.md")):
            with self.subTest(path=path):
                meta,body=metadata(path); name=meta.get("name","")
                self.assertRegex(name,SLUG)
                self.assertEqual(name,path.parent.name)
                self.assertNotIn(name,names); names.add(name)
                self.assertTrue(meta.get("description","").strip())
                self.assertLessEqual(len(meta["description"]),220)
                self.assertTrue(body.strip())

    def test_brand_assets_are_self_contained_square_svg(self):
        for name in ("logo-light.svg","logo-dark.svg","icon.svg"):
            path=ROOT/"assets"/name
            text=path.read_text(encoding="utf-8")
            self.assertIn('viewBox="0 0 100 100"',text)
            self.assertNotRegex(text,r"\bhref\s*=\s*['\"](?:https?:)?//|url\(\s*['\"]?(?:https?:)?//|<image\b|<script\b")

    def test_no_upstream_identity_or_credential_markers(self):
        forbidden=[
                        re.compile(r"(?i)\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
            re.compile(r"(?i)\bAKIA[0-9A-Z]{16}\b"),
        ]
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts: continue
            if path.suffix.lower() not in {".md",".py",".sh",".yml",".yaml",".txt",".svg"}: continue
            body=path.read_text(encoding="utf-8")
            for pattern in forbidden:
                with self.subTest(path=path,pattern=pattern.pattern):
                    self.assertIsNone(pattern.search(body))

    def test_project_documentation_and_scripts_exist(self):
        for path in (ROOT/"README.md",ROOT/"LICENSE",ROOT/"docs"/"compatibility.md",
                     ROOT/"scripts"/"install.sh",ROOT/"scripts"/"package_release.py",
                     ROOT/"scripts"/"validate_bundle.py"):
            self.assertTrue(path.is_file(),path)

    def test_release_zip_preserves_executable_entrypoints(self):
        with tempfile.TemporaryDirectory() as directory:
            archive=Path(directory)/"bundle.zip"
            result=subprocess.run(
                ["python3",str(ROOT/"scripts"/"package_release.py"),"--output",str(archive)],
                cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stdout+result.stderr)
            with ZipFile(archive) as z:
                for name in ("scripts/install.sh","scripts/validate_bundle.py","scripts/package_release.py"):
                    with self.subTest(name=name):
                        self.assertTrue((z.getinfo(name).external_attr>>16)&stat.S_IXUSR,name)

if __name__=="__main__": unittest.main()
