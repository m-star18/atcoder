def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    x, n = map(int, readline().split())
    p = list(map(int, readline().split()))
    check = float('inf')
    ans = 0
    for i in range(102):
        if i not in p:
            if check > abs(x - i):
                ans = i
                check = abs(x - i)
    print(ans)


if __name__ == '__main__':
    main()
