def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    d = int(readline())
    c = list(map(int, readline().split()))
    s = [list(map(int, readline().split())) for _ in range(d)]
    ans = 0
    memo = [0] * 26
    for i in range(1, d + 1):
        t = int(readline()) - 1
        ans += s[i - 1][t]
        memo[t] = i
        for m, cc in zip(memo, c):
            ans -= cc * (i - m)
        print(ans)


if __name__ == '__main__':
    main()
