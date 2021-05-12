def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    from copy import deepcopy

    d = int(readline())
    c = list(map(int, readline().split()))
    s = [list(map(int, readline().split())) for _ in range(d)]
    memo = [0] * 26
    check = 0
    for i in range(d):
        ans = 0
        tmp = deepcopy(check)
        check = -float('inf')
        for idx, ss in enumerate(s[i]):
            v = tmp + ss
            for j, (m, cc) in enumerate(zip(memo, c)):
                if j == idx:
                    continue
                v -= cc * (i + 1 - m)
            if check < v:
                ans = idx + 1
                check = v
        print(ans)
        memo[ans - 1] = i + 1


if __name__ == '__main__':
    main()
