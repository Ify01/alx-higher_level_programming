#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    
    loop = 0

    for t in range(len(sys.argv) - 1):
        loop += int(sys.argv[t + 1])
    print("{}".format(loop))

