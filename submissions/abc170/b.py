def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    x, y = map(int, readline().split())
    if 2 * x <= y <= 4 * x and y % 2 == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
