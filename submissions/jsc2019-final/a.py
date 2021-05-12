def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    from collections import defaultdict

    n, m = map(int, readline().split())
    a = list(map(int, readline().split()))
    b = list(map(int, readline().split()))
    dict = defaultdict(list)
    cnt = 0
    for i, aa in enumerate(a):
        for j, bb in enumerate(b):
            cnt += 1
            if dict[aa + bb]:
                print(*dict[aa + bb], i, j)
                exit()
            dict[aa + bb] = [i, j]
            if cnt > 2 * 10 ** 6:
                print(-1)
                exit()
    print(-1)


if __name__ == '__main__':
    main()
