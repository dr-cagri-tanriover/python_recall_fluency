from __future__ import annotations
from pathlib import Path
from typing import Iterator, Any, Dict, Optional, List
import os, json, shutil

def f01_read_text(path: str | Path, encoding: str = 'utf-8') -> str:
    '''
    >>> print(f"**** START f01_read_text() test ****")
    **** START f01_read_text() test ****
    >>> p = Path('io_tmp1.txt'); _ = p.write_text('hello', encoding='utf-8')
    >>> f01_read_text(p)
    'hello'
    >>> print(f"########################################")
    ########################################
    >>> p.unlink()
    '''  
    # WRITE YOUR SOLUTION HERE
    pass


def f02_write_text(path: str | Path, text: str, encoding: str = 'utf-8', newline: Optional[str] = '\\n') -> None:
    '''
    >>> print(f"**** START f02_write_text() test ****")
    **** START f02_write_text() test ****
    >>> p = Path('io_tmp2.txt')
    >>> sample_text = "a\\nb"
    >>> f02_write_text(p, sample_text, newline='\\n')
    >>> Path(p).read_text()
    'a\\nb'
    >>> print(f"########################################")
    ########################################
    >>> p.unlink()
    '''

    # WRITE YOUR SOLUTION HERE
    pass

def f03_append_text(path: str | Path, text: str, encoding: str = 'utf-8') -> None:
    '''
    >>> print(f"**** START f03_append_text() test ****")
    **** START f03_append_text() test ****
    >>> p = Path('io_tmp3.txt'); _ = p.write_text('a')
    >>> f03_append_text(p, 'b')
    >>> p.read_text()
    'ab'
    >>> print(f"########################################")
    ########################################
    >>> p.unlink()
    '''

    # WRITE YOUR SOLUTION HERE
    pass

def f04_read_bytes(path: str | Path) -> bytes:
    '''
    >>> print(f"**** START f04_read_bytes() test ****")
    **** START f04_read_bytes() test ****
    >>> p = Path('io_tmp4.bin'); _ = p.write_bytes(b'xyz')
    >>> f04_read_bytes(p)
    b'xyz'
    >>> print(f"########################################")
    ########################################
    >>> p.unlink()
    '''

    # WRITE YOUR SOLUTION HERE
    pass

def f05_write_bytes(path: str | Path, data: bytes) -> None:
    '''
    >>> print(f"**** START f05_write_bytes() test ****")
    **** START f05_write_bytes() test ****
    >>> p = Path('io_tmp5.bin')
    >>> f05_write_bytes(p, b'abc')
    >>> p.read_bytes()
    b'abc'
    >>> print(f"########################################")
    ########################################
    >>> p.unlink()
    '''

    # WRITE YOUR SOLUTION HERE
    pass

def f06_ensure_dir(path: str | Path, exist_ok: bool = True) -> Path:
    '''
    >>> print(f"**** START f06_ensure_dir() test ****")
    **** START f06_ensure_dir() test ****
    >>> d = Path('io_tmpdir1')
    >>> _ = f06_ensure_dir(d)
    >>> d.is_dir()
    True
    >>> d.rmdir()
    >>> print(f"########################################")
    ########################################
    '''

    # WRITE YOUR SOLUTION HERE
    pass


def f07_list_files_glob(directory: str | Path, pattern: str = '*.py') -> List[Path]:
    '''
    >>> print(f"**** START f07_list_files_glob() test ****")
    **** START f07_list_files_glob() test ****
    >>> d = Path('io_glob'); d.mkdir(exist_ok=True)
    >>> _ = (d/'a.py').write_text('')
    >>> _ = (d/'b.txt').write_text('')
    >>> [p.name for p in f07_list_files_glob(d, '*.py')]
    ['a.py']
    >>> (d/'a.py').unlink(); (d/'b.txt').unlink(); d.rmdir()
    >>> print(f"########################################")
    ########################################
    '''

    # WRITE YOUR SOLUTION HERE
    pass

def f08_walk_files(directory: str | Path) -> List[Path]:
    '''
    >>> print(f"**** START f08_walk_files() test ****")
    **** START f08_walk_files() test ****
    >>> d = Path('io_walk'); d.mkdir(exist_ok=True)
    >>> _ = (d/'a.txt').write_text('x')
    >>> sub = d/'sub'; sub.mkdir(exist_ok=True)
    >>> _ = (sub/'b.txt').write_text('y')
    >>> sorted([p.as_posix() for p in f08_walk_files(d)])
    ['io_walk/a.txt', 'io_walk/sub/b.txt']
    >>> (sub/'b.txt').unlink(); sub.rmdir(); (d/'a.txt').unlink(); d.rmdir()
    >>> print(f"########################################")
    ########################################
    '''

    # WRITE YOUR SOLUTION HERE
    pass


def f09_copy_file(src: str | Path, dst: str | Path) -> Path:
    '''
    >>> print(f"**** START f09_copy_file() test ****")
    **** START f09_copy_file() test ****
    >>> s = Path('io_src.txt'); _ = s.write_text('hi')
    >>> d = Path('io_dst.txt')
    >>> f09_copy_file(s, d).read_text()
    'hi'
    >>> s.unlink(); d.unlink()
    >>> print(f"########################################")
    ########################################
    '''

    # WRITE YOUR SOLUTION HERE
    pass

def f10_move_file(src: str | Path, dst: str | Path) -> Path:
    '''
    >>> print(f"**** START f10_move_file() test ****")
    **** START f10_move_file() test ****
    >>> s = Path('io_msrc.txt'); _ = s.write_text('hi')
    >>> d = Path('io_mdst.txt')
    >>> f10_move_file(s, d).read_text()
    'hi'
    >>> d.unlink()
    >>> s.unlink()
    >>> print(f"########################################")
    ########################################
    '''

    # WRITE YOUR SOLUTION HERE
    pass

def f11_delete_file(path: str | Path, missing_ok: bool = True) -> None:
    '''
    >>> print(f"**** START f11_delete_file() test ****")
    **** START f11_delete_file() test ****
    >>> p = Path('io_del.txt'); _ = p.write_text('x')
    >>> f11_delete_file(p); p.exists()
    False
    >>> f11_delete_file('no_such_file.txt', missing_ok=True)
    >>> p.unlink()
    >>> print(f"########################################")
    ########################################
    '''

    # WRITE YOUR SOLUTION HERE
    pass


def f12_iter_byte_chunks(path: str | Path, size: int = 8192) -> Iterator[bytes]:
    '''
    >>> print(f"**** START f12_iter_byte_chunks() test ****")
    **** START f12_iter_byte_chunks() test ****
    >>> p = Path('io_chunk.bin'); _ = p.write_bytes(b'abcdefghij')
    >>> [len(c) for c in f12_iter_byte_chunks(p, 4)]
    [4, 4, 2]
    >>> p.unlink()
    >>> print(f"########################################")
    ########################################
    '''

    # WRITE YOUR SOLUTION HERE
    pass


def f13_json_load(path: str | Path) -> Dict[str, Any]:
    '''
    >>> print(f"**** START f13_json_load() test ****")
    **** START f13_json_load() test ****
    >>> p = Path('io.json'); _ = p.write_text('{"a":1,"b":2}', encoding='utf-8')
    >>> f13_json_load(p)['b']
    2
    >>> p.unlink()
    >>> print(f"########################################")
    ########################################
    '''

    # WRITE YOUR SOLUTION HERE
    pass

def f14_json_dump_pretty(path: str | Path, obj: Dict[str, Any]) -> None:
    '''
    >>> print(f"**** START f14_json_dump_pretty() test ****")
    **** START f14_json_dump_pretty() test ****
    >>> p = Path('io_out.json')
    >>> f14_json_dump_pretty(p, {'x': 1})
    >>> '"x": 1' in p.read_text()
    True
    >>> p.unlink()
    >>> print(f"########################################")
    ########################################
    '''

    # WRITE YOUR SOLUTION HERE
    pass


def f15_get_cwd() -> Path:
    '''
    >>> print(f"**** START f15_get_cwd() test ****")
    **** START f15_get_cwd() test ****
    >>> isinstance(f15_get_cwd(), Path)
    True
    >>> print(f"########################################")
    ########################################
    '''

    # WRITE YOUR SOLUTION HERE
    pass


def f16_read_env(name: str, default: Optional[str] = None) -> Optional[str]:
    '''
    >>> print(f"**** START f16_read_env() test ****")
    **** START f16_read_env() test ****
    >>> _ = os.environ.setdefault('X_EXAMPLE', '42')
    >>> f16_read_env('X_EXAMPLE')
    '42'
    >>> print(f"########################################")
    ########################################
    '''
    
    # WRITE YOUR SOLUTION HERE
    pass
