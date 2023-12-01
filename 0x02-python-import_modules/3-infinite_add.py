#!/usr/bin/python3

if __name__ == "__main__":
    import sys


    looping = 0

    for arg in sys.argv[1:]:
        looping += int(arg)

    print(looping)
