import re
import sys


def parse_file(path):
    with open("temp.py") as f:
        out = re.sub(r"^\d+|^ \d+","",f.read(),flags=re.MULTILINE)
    if path and out:
        try:
            u = open(path)
            u.close()
            print("File already exists")
        except FileNotFoundError:
            with open(path,"w") as f:
                f.write(out)
        



if __name__ == "__main__":
    print(sys.argv)
    path = sys.argv[1] if len(sys.argv) == 2 else None
    parse_file(path=path)