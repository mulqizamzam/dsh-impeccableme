#!/usr/bin/env python3
"""Dependency-free validation for DSH Design Workbench."""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path
from xml.etree import ElementTree

ROOT=Path(__file__).resolve().parents[1]
SKILLS=ROOT/".dsh"/"skills"
SLUG=re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SECRETS=[
 re.compile(r"(?i)\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
 re.compile(r"(?i)\bAKIA[0-9A-Z]{16}\b"),
 re.compile(r"(?i)-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]
UPSTREAM=[
 re.compile(r"(?i)\b"+"pba"+"kaus"+r"\b"),
 re.compile(r"(?i)"+"impec"+"cable"+r"\.style"),
 re.compile(r"(?i)"+"renaissance-"+"geek"),
]

def parse_frontmatter(text: str, path: Path):
 if not text.startswith("---\n"):
  raise ValueError(f"{path}: missing YAML frontmatter start")
 end=text.find("\n---\n",4)
 if end<0:
  raise ValueError(f"{path}: missing YAML frontmatter end")
 data={}
 for i,line in enumerate(text[4:end].splitlines(),2):
  if not line.strip() or line.lstrip().startswith("#"): continue
  if line[:1].isspace() or ":" not in line:
   raise ValueError(f"{path}:{i}: unsupported frontmatter line")
  key,value=line.split(":",1); key=key.strip(); value=value.strip()
  if not key or not value or key in data:
   raise ValueError(f"{path}:{i}: empty or duplicate metadata")
  if value.startswith(("&","*","!","|",">","{","[")):
   raise ValueError(f"{path}:{i}: complex YAML not allowed")
  if value[:1] in ("'",'"'):
   if len(value)<2 or value[-1]!=value[0]:
    raise ValueError(f"{path}:{i}: malformed quoted scalar")
   value=value[1:-1]
  data[key]=value
 return data,text[end+5:]

def inspect_skills():
 errors=[]
 if not SKILLS.is_dir(): return ["missing .dsh/skills"]
 entries=sorted(SKILLS.iterdir(),key=lambda p:p.name)
 if len(entries)!=8: errors.append(f"expected 8 Skills, found {len(entries)}")
 names=set()
 for d in entries:
  rel=d.relative_to(ROOT).as_posix()
  if d.is_symlink() or not d.is_dir():
   errors.append(f"invalid Skill entry: {rel}"); continue
  if not SLUG.fullmatch(d.name): errors.append(f"invalid Skill slug: {rel}")
  sf=d/"SKILL.md"
  if not sf.is_file() or sf.is_symlink():
   errors.append(f"missing regular SKILL.md: {rel}"); continue
  try:
   raw=sf.read_text(encoding="utf-8"); meta,body=parse_frontmatter(raw,sf)
   name=meta.get("name",""); desc=meta.get("description","")
   if not SLUG.fullmatch(name): errors.append(f"{rel}: invalid metadata name")
   if name!=d.name: errors.append(f"{rel}: name does not match directory")
   if name in names: errors.append(f"{rel}: duplicate Skill name")
   if not desc or len(desc)>220: errors.append(f"{rel}: missing/long description")
   if not body.strip(): errors.append(f"{rel}: empty instructions")
   names.add(name)
   for match in re.findall(r"\[[^\]]+\]\(([^)]+)\)",body):
    if match.startswith(("https://","http://","mailto:","#")): continue
    dest=(sf.parent/match.split("#",1)[0]).resolve()
    if not dest.exists(): errors.append(f"{rel}: broken local link {match}")
    elif ROOT not in dest.parents and dest!=ROOT: errors.append(f"{rel}: local link escapes package")
  except (OSError,UnicodeError,ValueError) as exc: errors.append(str(exc))
 return errors

def inspect_public_files():
 errors=[]
 for p in ROOT.rglob("*"):
  if ".git" in p.parts or "__pycache__" in p.parts or not p.is_file(): continue
  rel=p.relative_to(ROOT).as_posix()
  if p.is_symlink(): errors.append(f"symlink not allowed: {rel}"); continue
  if p.suffix.lower() not in {".md",".py",".sh",".yml",".yaml",".json",".txt",".svg",".gitignore"} and p.name!="VERSION": continue
  try: body=p.read_text(encoding="utf-8")
  except (OSError,UnicodeError): errors.append(f"unreadable/non-UTF8: {rel}"); continue
  if any(rx.search(body) for rx in UPSTREAM): errors.append(f"prohibited upstream identity marker: {rel}")
  if any(rx.search(body) for rx in SECRETS): errors.append(f"credential-shaped value: {rel}")
  if p.suffix.lower()==".svg":
   try:
    root=ElementTree.fromstring(body)
    vb=[float(x) for x in root.attrib.get("viewBox","").replace(","," ").split()]
    if not root.tag.endswith("svg") or len(vb)!=4 or vb[2]<=0 or vb[3]<=0 or vb[2]!=vb[3]:
     errors.append(f"SVG viewBox must be square: {rel}")
   except (ElementTree.ParseError,ValueError): errors.append(f"invalid SVG: {rel}")
   if re.search(r"\bhref\s*=\s*['\"](?:https?:)?//|url\(\s*['\"]?(?:https?:)?//|<image\b|<script\b",body,re.I):
    errors.append(f"external/script SVG content: {rel}")
 return errors


def inspect_dsh_bundle():
 errors=[]
 try:
  manifest=json.loads((ROOT/"package.json").read_text(encoding="utf-8"))
 except (OSError,UnicodeError,ValueError):
  return ["package.json is missing or invalid JSON"]
 if manifest.get("name")!="dsh-impeccableme": errors.append("package.json: wrong bundle name")
 if manifest.get("version")!="0.1.0": errors.append("package.json: version must match VERSION")
 if manifest.get("main")!="index.js" or not (ROOT/"index.js").is_file(): errors.append("package.json: missing index.js entrypoint")
 if manifest.get("engines",{}).get("dsh")!=">=0.2.1-rc.2 <0.3.0": errors.append("package.json: wrong DSH engine range")
 if manifest.get("dsh",{}).get("bundle",{}).get("patch")!="./cordis.patch.yml": errors.append("package.json: missing dsh.bundle.patch")
 expected={"index.js","cordis.patch.yml",".dsh/skills/**"}
 if not expected.issubset(set(manifest.get("files",[]))): errors.append("package.json: files must include entrypoint, patch, and Skill sources")
 patch_path=ROOT/"cordis.patch.yml"
 try: patch=patch_path.read_text(encoding="utf-8")
 except (OSError,UnicodeError): return errors+["cordis.patch.yml is missing or unreadable"]
 for pattern,label in ((r"(?m)^-\s+insert:\s*$","insert operation"),
                       (r"(?m)^\s+- id:\s*dsh-impeccableme\s*$","bundle row ID"),
                       (r"(?m)^\s+name:\s*dsh-impeccableme\s*$","plugin entrypoint row")):
  if not re.search(pattern,patch): errors.append("cordis.patch.yml: missing "+label)
 return errors

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument("--quiet",action="store_true")
 parser.parse_args()
 errors=inspect_skills()+inspect_dsh_bundle()+inspect_public_files()
 if errors:
  print("Bundle validation: FAIL")
  for error in errors: print(" - "+error)
  return 1
 print("Bundle validation: PASS (8 Skills)")
 return 0
if __name__=="__main__": sys.exit(main())
