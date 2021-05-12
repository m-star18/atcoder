def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    def check(m):
        for bf, c, af, ss in zip(m, m[1:], m[2:], s):
            if ss == 'o':
                if (c == 'S' and bf != af) or (c == 'W' and bf == af):
                    return False
            else:
                if (c == 'S' and bf == af) or (c == 'W' and bf != af):
                    return False
        return True

    n = int(readline())
    s = readline().rstrip().decode()
    flag = {'S': 'W', 'W': 'S'}
    for m in ('SS', 'SW', 'WS', 'WW'):
        for i, ss in enumerate(s[1:-1]):
            if ss == 'o':
                if m[i + 1] == 'S':
                    m += m[i]
                else:
                    m += flag[m[i]]
            else:
                if m[i + 1] == 'S':
                    m += flag[m[i]]
                else:
                    m += m[i]
        if check(m[-1] + m + m[0]):
            print(m)
            break
    else:
        print(-1)


if __name__ == '__main__':
    main()
