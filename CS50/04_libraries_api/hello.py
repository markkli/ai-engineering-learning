import sys

if len(sys.argv) < 2:
    sys.exit("too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("too many command-line arguments")
print("hello, my name is", sys.argv[1])