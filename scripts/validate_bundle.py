#!/usr/bin/env python3
"""Dependency-free structural and public-safety checks for DSH Skills."""
from pathlib import Path
import re,sys
from xml.etree import ElementTree
ROOT=Path(__file__).resolve().parents[1]; SKILLS=ROOT/".dsh"/"skills"; SLUG=re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FORBIDDEN=[re.compile(r"(?i)\bgh[pousr]_[A-Za-z0-9]{20,}\b"),re.compile(r"(?i)\bAKIA[0-9A-Z]{16}\b"),re.compile(r"(?i)-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")]
def metadata(text,path):
 if not text.startswith("---\n"): raise ValueError(f"{path}: missing frontmatter")
 end=text.find("\n---\n",4)
 if end<0: raise ValueError(f"{path}: missing closing frontmatter")
 data={}
 for line in text[4:end].splitlines():
  if not line.strip() or line.lstrip().startswith("#"): continue
  k,sep,v=line.partition(":")
  if not sep or not k.strip() or not v.strip() or k.strip() in data: raise ValueError(f"{path}: invalid metadata line")
  data[k.strip()]=v.strip().strip("\"'")
 return data,text[end+5:]
def main():
 errors=[]
 if not SKILLS.is_dir(): errors.append("missing .dsh/skills")
 else:
  children=sorted(SKILLS.iterdir()); names=set()
  if len(children)!=8: errors.append(f"expected 8 direct Skills, found {len(children)}")
  for d in children:
   if d.is_symlink() or not d.is_dir(): errors.append(f"invalid Skill entry: {d}"); continue
   sf=d/"SKILL.md"
   if not sf.is_file() or sf.is_symlink(): errors.append(f"missing SKILL.md: {d}"); continue
   try:
    meta,body=metadata(sf.read_text(encoding="utf-8"),sf); name=meta.get("name",""); desc=meta.get("description","")
    if not SLUG.fullmatch(d.name) or name!=d.name or name in names or not desc or len(desc)>220 or not body.strip(): errors.append(f"invalid metadata/body: {sf}")
    names.add(name)
   except Exception as e: errors.append(str(e))
 for p in ROOT.rglob("*"):
  if ".git" in p.parts or "__pycache__" in p.parts or not p.is_file(): continue
  if p.is_symlink(): errors.append(f"symlink: {p}"); continue
  if p.suffix.lower() in {".md",".py",".sh",".yml",".yaml",".json",".txt",".svg"}:
   try: text=p.read_text(encoding="utf-8")
   except Exception: errors.append(f"non UTF-8: {p}"); continue
   for rx in FORBIDDEN:
    if rx.search(text): errors.append(f"credential-like content: {p}")
   if p.suffix.lower()==".svg":
    try:
     root=ElementTree.fromstring(text); vb=[float(x) for x in root.attrib.get("viewBox","").replace(","," ").split()]
     if not root.tag.endswith("svg") or len(vb)!=4 or vb[2]<=0 or vb[3]<=0 or vb[2]!=vb[3]: errors.append(f"bad square SVG: {p}")
    except Exception: errors.append(f"bad SVG: {p}")
 if errors:
  print("Bundle validation: FAIL"); print("\n".join(" - "+e for e in errors)); return 1
 print("Bundle validation: PASS (8 Skills)"); return 0
if __name__=="__main__": sys.exit(main())
