
from pathlib import Path
import os

def main():
    '''
    Use this space as sandbox for quick testing
    '''

    path = "./"

    for r,s,f in os.walk(Path(path)):
        if not r.startswith('./.'):
            print(f"{r} {s} {f}")

if __name__ == "__main__":
    main()
