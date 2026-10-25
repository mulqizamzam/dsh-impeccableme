from pathlib import Path
import re, stat, subprocess, tempfile, unittest
from zipfile import ZipFile
ROOT=Path(__file__).resolve().parents[1]; SKILLS=ROOT/".dsh"/"skills"; SLUG=re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
def metadata(path):
 text=path.read_text(encoding="utf-8"); end=text.find("\n---\n",4)
 if not text.startswith("---\n") or end<0: raise AssertionError(f"bad frontmatter: {path}")
 data={}
 for line in text[4:end].splitlines():
  k,sep,v=line.partition(":")
  if sep and k.strip() and v.strip(): data[k.strip()]=v.strip().strip("\"'")
 return data,text[end+5:]
class BundleTests(unittest.TestCase):
 def test_eight_skills(self):
  dirs=sorted(p for p in SKILLS.iterdir()); self.assertEqual(len(dirs),8)
  for d in dirs: self.assertTrue(d.is_dir()); self.assertTrue((d/"SKILL.md").is_file()); self.assertRegex(d.name,SLUG)
 def test_metadata(self):
  names=set()
  for p in SKILLS.glob("*/SKILL.md"):
   m,b=metadata(p); self.assertRegex(m.get("name",""),SLUG); self.assertEqual(m["name"],p.parent.name); self.assertNotIn(m["name"],names); names.add(m["name"]); self.assertTrue(m.get("description")); self.assertTrue(b.strip())
 def test_assets(self):
  for name in ("icon.svg","logo-light.svg","logo-dark.svg"):
   p=ROOT/"assets"/name; text=p.read_text(); self.assertIn('viewBox="0 0 100 100"',text); self.assertNotRegex(text,r"<script|<image|https?://[^\s\"]+")
 def test_no_upstream_or_secret_markers(self):
  for p in ROOT.rglob("*"):
   if not p.is_file() or ".git" in p.parts or "__pycache__" in p.parts: continue
   if p.suffix.lower() not in {".md",".py",".sh",".yml",".yaml",".svg"}: continue
   s=p.read_text(); self.assertNotRegex(s,r"(?i)\b(?:pba|kaus)\b|impeccable\.style|renaissance-geek|\bgh[pousr]_[A-Za-z0-9]{20,}\b|\bAKIA[0-9A-Z]{16}\b")
 def test_project_files(self):
  for p in (ROOT/"README.md",ROOT/"LICENSE",ROOT/"scripts"/"install.sh",ROOT/"scripts"/"package_release.py"): self.assertTrue(p.is_file())
 def test_zip_modes(self):
  with tempfile.TemporaryDirectory() as t:
   z=Path(t)/"p.zip"; r=subprocess.run(["python3",str(ROOT/"scripts"/"package_release.py"),"--output",str(z)],capture_output=True,text=True); self.assertEqual(r.returncode,0,r.stdout+r.stderr)
   with ZipFile(z) as a:
    for n in ("scripts/install.sh","scripts/validate_bundle.py","scripts/package_release.py"):
     self.assertTrue((a.getinfo(n).external_attr>>16)&stat.S_IXUSR,n)
if __name__=="__main__": unittest.main()
