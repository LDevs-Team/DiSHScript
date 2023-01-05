import scripting
import sys

if __name__ == "__main__":
    f = sys.argv[2]
    buf = open(f, "r")
    tokens = scripting.parse(f.read())
    buf.close()
    scripting.run(tokens)