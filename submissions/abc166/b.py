def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    n, k = map(int, readline().split())
    memo = set()
    cnt = 0
    for _ in range(k):
        d = int(readline())
        memo |= set(map(int, readline().split()))
    for i in range(1, n + 1):
        if i not in memo:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
