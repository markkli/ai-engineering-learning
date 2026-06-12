from sayings import hello
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python say.py [name]")

hello(sys.argv[1])