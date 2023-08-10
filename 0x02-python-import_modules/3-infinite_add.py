#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    addition = 0
    if n == 0:
        print("0")
    elif n == 1:
        print("{}".format(sys.argv[1]))
    else:
        for i in range(n):
            addition += int(sys.argv[i + 1])
        print("{}".format(addition))
