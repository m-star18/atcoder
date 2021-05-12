def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    from collections import defaultdict

    n = int(readline())
    dp = [0] * (n + 1)
    dp[0] = 1
    memo = defaultdict(int)
    mod = 10 ** 9 + 7
    for i in range(1, n + 1):
        c = int(readline())
        dp[i] = dp[i - 1]
        if 0 < memo[c] < i - 1:
            dp[i] += dp[memo[c]]
        memo[c] = i
        dp[i] %= mod
    print(dp[n])


if __name__ == '__main__':
    main()
