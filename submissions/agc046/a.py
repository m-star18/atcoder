def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    from math import gcd

    x = int(readline())
    print(360 // gcd(x, 360))


if __name__ == '__main__':
    main()
