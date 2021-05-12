def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    n, k = map(int, readline().split())
    p = list(map(int, readline().split()))
    p.sort()
    print(sum(p[:k]))


if __name__ == '__main__':
    main()
