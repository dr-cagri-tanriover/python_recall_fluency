from __future__ import annotations
from pathlib import Path
from typing import Iterator, Any, Dict, Optional, List
import os, json, shutil, tempfile, hashlib

def f01_read_text(path: str | Path, encoding: str = 'utf-8') -> str:
    return Path(path).read_text(encoding=encoding)

def f02_write_text(path: str | Path, text: str, encoding: str = 'utf-8', newline: Optional[str] = '\n') -> None:
    with open(path, 'w', encoding=encoding, newline=newline) as f:
        f.write(text)

def f03_append_text(path: str | Path, text: str, encoding: str = 'utf-8') -> None:
    with open(path, 'a', encoding=encoding) as f:
        f.write(text)

def f04_read_bytes(path: str | Path) -> bytes:
    return Path(path).read_bytes()

def f05_write_bytes(path: str | Path, data: bytes) -> None:
    Path(path).write_bytes(data)

def f06_atomic_write_text(path: str | Path, text: str, encoding: str = 'utf-8') -> None:
    path = Path(path)
    with tempfile.NamedTemporaryFile('w', encoding=encoding, delete=False, dir=path.parent) as tmp:
        tmp.write(text)
        tmp_path = Path(tmp.name)
    os.replace(tmp_path, path)

def f07_ensure_dir(path: str | Path, exist_ok: bool = True) -> Path:
    p = Path(path); p.mkdir(parents=True, exist_ok=exist_ok); return p

def f08_list_files_glob(directory: str | Path, pattern: str = '*.py') -> List[Path]:
    return list(Path(directory).glob(pattern))

def f09_walk_files(directory: str | Path) -> List[Path]:
    out: List[Path] = []
    for root, subdir_names_under_root , files_under_root in os.walk(directory):
        for name in files_under_root:
            out.append(Path(root) / name)
    return out

def f10_copy_file(src: str | Path, dst: str | Path) -> Path:
    return Path(shutil.copy2(src, dst))

def f11_move_file(src: str | Path, dst: str | Path) -> Path:
    return Path(shutil.move(src, dst))

def f12_delete_file(path: str | Path, missing_ok: bool = True) -> None:
    
    #OPTION 1:
    try:
        Path(path).unlink()
    except FileNotFoundError:
        if not missing_ok: raise

    '''
    #OPTION 2:
    try:
        os.remove(path)
    except FileNotFounderror:
        if not missing_ok:
            raise
    '''


def f13_iter_byte_chunks(path: str | Path, size: int = 8192) -> Iterator[bytes]:
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(size)
            if not chunk: break
            yield chunk

def f14_md5_of_file(path: str | Path) -> str:
    h = hashlib.md5()
    for c in iter_chunks(path, 8192): h.update(c)
    return h.hexdigest()

def f15_json_load(path: str | Path) -> Dict[str, Any]:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def f16_json_dump_pretty(path: str | Path, obj: Dict[str, Any]) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)

def f17_jsonl_read(path: str | Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows

def f18_jsonl_append(path: str | Path, obj: Dict[str, Any]) -> None:
    with open(path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(obj, ensure_ascii=False) + '\n')

def f19_get_cwd() -> Path:
    return Path.cwd()

def f20_read_env(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.environ.get(name, default)

def f21_resolve_symlink(path: str | Path) -> Path:
    return Path(path).resolve()
