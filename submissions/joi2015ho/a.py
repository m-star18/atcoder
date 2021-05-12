def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    from itertools import accumulate

    n, m = map(int, readline().split())
    p = list(map(int, readline().split()))
    cumsum = [0] * (n + 1)
    for bf, af in zip(p, p[1:]):
        if bf > af:
            bf, af = af, bf
        cumsum[bf] += 1
        cumsum[af] -= 1
    cumsum = list(accumulate(cumsum))
    ans = 0
    for v in cumsum[1:-1]:
        a, b, c = map(int, readline().split())
        ans += min(a * v, b * v + c)
    print(ans)


if __name__ == '__main__':
    main()
