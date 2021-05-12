def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    n = int(readline())
    a = list(map(int, readline().split()))
    memo = 0
    for aa in a:
        memo ^= aa
    for i in range(n):
        a[i] ^= memo
    print(*a)


if __name__ == '__main__':
    main()
