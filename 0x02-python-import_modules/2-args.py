#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    i = 0
    if n == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(n))
    for i in range(n):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
