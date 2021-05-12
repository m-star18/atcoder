def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    from collections import Counter

    n = int(readline())
    a = list(map(int, readline().split()))
    ans = sum(a)
    counter = Counter(a)
    q = int(readline())
    for _ in range(q):
        b, c = map(int, readline().split())
        ans += (c - b) * counter[b]
        counter[c] += counter[b]
        counter[b] = 0
        print(ans)


if __name__ == '__main__':
    main()
