#!/usr/bin/env python3
"""Build a deterministic ZIP distribution for the DSH Skill package."""
from __future__ import annotations
import argparse, hashlib, os, stat, sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo
ROOT=Path(__file__).resolve().parents[1]
EXCLUDED_DIRS={".git","__pycache__",".pytest_cache",".mypy_cache",".ruff_cache","dist",".coverage-data"}
FIXED_TIME=(2020,1,1,0,0,0)
def sha256(path:Path)->str:
 h=hashlib.sha256()
 with path.open("rb") as f:
  for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
 return h.hexdigest()
def collect_files():
 out=[]
 for p in ROOT.rglob("*"):
  rel=p.relative_to(ROOT)
  if any(part in EXCLUDED_DIRS for part in rel.parts): continue
  if p.is_symlink(): raise ValueError(f"symlink not allowed: {rel}")
  if not p.is_file() or p.name in {".DS_Store","Thumbs.db"} or p.suffix in {".pyc",".pyo",".zip"}: continue
  out.append(p)
 return sorted(out,key=lambda p:p.relative_to(ROOT).as_posix())
def package(output:Path):
 output=output.expanduser()
 if output.is_symlink(): raise ValueError("output must not be a symlink")
 output=output.resolve()
 if output==ROOT or ROOT in output.parents: raise ValueError("output must be outside source tree")
 output.parent.mkdir(parents=True,exist_ok=True); files=collect_files(); tmp=output.with_name(output.name+".tmp")
 if tmp.is_symlink(): raise ValueError("temporary output must not be a symlink")
 if tmp.exists(): tmp.unlink()
 with ZipFile(tmp,"w",compression=ZIP_DEFLATED,compresslevel=9,strict_timestamps=True) as z:
  for p in files:
   info=ZipInfo(p.relative_to(ROOT).as_posix(),date_time=FIXED_TIME); info.compress_type=ZIP_DEFLATED; info.create_system=3
   mode=0o755 if (p.stat().st_mode & stat.S_IXUSR) or p.suffix in {".sh", ".py"} and p.parts[-2] == "scripts" else 0o644; info.external_attr=((stat.S_IFREG|mode)<<16) | 0x10; info.flag_bits|=0x800; info.extra=b""; info.comment=b""
   z.writestr(info,p.read_bytes(),compress_type=ZIP_DEFLATED,compresslevel=9)
 os.replace(tmp,output); return len(files),sha256(output)
def main():
 ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--output",required=True); args=ap.parse_args()
 try: count,digest=package(Path(args.output))
 except (OSError,ValueError) as e: print(f"package failed: {e}",file=sys.stderr); return 1
 print(f"Package: {Path(args.output).expanduser().resolve()}\nFiles: {count}\nSHA256: {digest}"); return 0
if __name__=="__main__": sys.exit(main())
