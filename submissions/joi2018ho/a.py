def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    n, m = map(int, readline().split())
    t = [int(readline()) for _ in range(n)]
    t.sort()
    memo = [0] * (n - 1)
    for i, (bf, af) in enumerate(zip(t, t[1:])):
        memo[i] = max(0, af - bf - 1)
    memo.sort(reverse=True)
    print(t[-1] + 1 - t[0] - sum(memo[:m - 1]))


if __name__ == '__main__':
    main()
