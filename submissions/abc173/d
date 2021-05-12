def main():
    import sys
    readline = sys.stdin.buffer.readline
    sys.setrecursionlimit(10 ** 7)

    n = int(readline())
    a = list(map(int, readline().split()))
    a.sort(reverse=True)
    idx = 1
    ans = a[0]
    for aa in a[1:]:
        if idx + 2 >= n:
            if idx + 1 < n:
                ans += aa
            break
        idx += 2
        ans += aa * 2
    print(ans)


if __name__ == '__main__':
    main()
