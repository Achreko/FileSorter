import os
from pathlib import Path
from datetime import datetime
# import re

def do(suffix="\*"):
    pth = Path('test')
    for file in list(Path(pth).iterdir()):
        scr = Path(file)
        scr.resolve()
        print(scr.stat())
        os.rename(file, f'{file}_{datetime.fromtimestamp(scr.stat().st_atime)})')
        


if __name__ == "__main__":
    do()