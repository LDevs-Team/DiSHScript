import scripting
import sys

if __name__ == "__main__":
    f = sys.argv[1]
    buf = open(f, "r")
    tokens = scripting.parse(buf.read())
    buf.close()
    scripting.run(tokens, {})