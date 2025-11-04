from __future__ import annotations
from pathlib import Path
from typing import Iterator, Any, Dict, Optional, List
import os, json, shutil

def f01_read_text(path: str | Path, encoding: str = 'utf-8') -> str:
    return Path(path).read_text(encoding=encoding)

    '''OPTION 2
    with open(path, 'r', encoding=encoding) as f:
        return f.read()
    '''

def f02_write_text(path: str | Path, text: str, encoding: str = 'utf-8', newline: Optional[str] = '\n') -> None:
    with open(path, 'w', encoding=encoding, newline=newline) as f:
        f.write(text)
    
    ''' OPTION 2
    Path(path).write_text(text, encoding=encoding, newline=newline)
    '''

def f03_append_text(path: str | Path, text: str, encoding: str = 'utf-8') -> None:
    with open(path, 'a', encoding=encoding) as f:
        f.write(text)

def f04_read_bytes(path: str | Path) -> bytes:
    return Path(path).read_bytes()

    ''' OPTION 2
    with open(path, 'rb') as f:
        return f.read()
    '''

def f05_write_bytes(path: str | Path, data: bytes) -> None:
    Path(path).write_bytes(data)

    ''' OPTION 2
    with open(path, 'wb') as f:
        f.write(data)
    '''


def f06_ensure_dir(path: str | Path, exist_ok: bool = True) -> Path:
    p = Path(path); p.mkdir(parents=True, exist_ok=exist_ok); return p

def f07_list_files_glob(directory: str | Path, pattern: str = '*.py') -> List[Path]:
    return list(Path(directory).glob(pattern))

def f08_walk_files(directory: str | Path) -> List[Path]:
    out: List[Path] = []
    for root, subdir_names_under_root , files_under_root in os.walk(directory):
        for name in files_under_root:
            out.append(Path(root) / name)
    return out

def f09_copy_file(src: str | Path, dst: str | Path) -> Path:
    return Path(shutil.copy2(src, dst))

def f10_move_file(src: str | Path, dst: str | Path) -> Path:
    return Path(shutil.move(src, dst))

def f11_delete_file(path: str | Path, missing_ok: bool = True) -> None:
    
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


def f12_iter_byte_chunks(path: str | Path, size: int = 8192) -> Iterator[bytes]:
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(size)
            if not chunk: break
            yield chunk

def f13_json_load(path: str | Path) -> Dict[str, Any]:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def f14_json_dump_pretty(path: str | Path, obj: Dict[str, Any]) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
    
    # indent ='\t' also accepted
    # ensure_ascii = False does not escape non-ASCII characters - better for human readability.


def f15_get_cwd() -> Path:
    return Path.cwd()

def f16_read_env(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.environ.get(name, default)  # read the environment variable name, if it exists. Otherwise, return default. (wihout default, None will be returned)

    # os.environ.setdefault('VAR', '42')  # sets VAR to '42' in the environment IF key does not exist. Otherwise, it returns its existing value.
    # os.environ.pop(name, None)  # deletes environment variable name. Does nothing if missing.


