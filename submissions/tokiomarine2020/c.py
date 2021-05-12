def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    from itertools import accumulate

    n, k = map(int, readline().split())
    a = [*map(int, readline().split())]
    for _ in range(min(k, 41)):
        memo = [0] * n
        for i, aa in enumerate(a):
            if i > aa:
                memo[i - aa] += 1
            else:
                memo[0] += 1
            j = i - ~ aa
            if j < n:
                memo[j] -= 1
        a = [*accumulate(memo)]
    print(*a)


if __name__ == '__main__':
    main()
