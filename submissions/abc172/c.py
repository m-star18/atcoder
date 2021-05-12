def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    from itertools import accumulate
    from bisect import bisect_right

    n, m, k = map(int, readline().split())
    a = [0] + list(accumulate(map(int, readline().split())))
    b = list(accumulate(map(int, readline().split())))
    ans = 0
    for i, aa in enumerate(a):
        if k < aa:
            break
        ans = max(ans, bisect_right(b, k - aa) + i)
    print(ans)


if __name__ == '__main__':
    main()
