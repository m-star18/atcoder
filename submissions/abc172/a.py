def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    a = int(readline())
    print(a + a ** 2 + a ** 3)


if __name__ == '__main__':
    main()
