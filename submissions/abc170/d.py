def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    n = int(readline())
    a = list(map(int, readline().split()))
    a.sort()
    limit = a[-1]
    dp = [0] * (limit + 1)
    for aa in a:
        dp[aa] += 1
        if dp[aa] == 1:
            for i in range(aa * 2, limit + 1, aa):
                dp[i] += 1
    print(sum((1 for aa in a if dp[aa] == 1)))


if __name__ == '__main__':
    main()
