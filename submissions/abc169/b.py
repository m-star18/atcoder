def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    n = int(readline())
    a = list(map(int, readline().split()))
    a.sort()
    ans = 1
    for aa in a:
        ans *= aa
        if ans > 10 ** 18:
            print(-1)
            break
    else:
        print(ans)


if __name__ == '__main__':
    main()
