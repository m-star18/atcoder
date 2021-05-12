def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    n = int(readline())
    s = readline().rstrip().decode()
    q = set(s[0])
    for ss in s[1:]:
        x = set()
        y = set()
        flag = True
        while q:
            m = q.pop()
            if m == '':
                x.add(ss)
                break
            if m[0] == ss:
                flag = False
                x.add(m[1:])
            else:
                y.add(ss + m)
            if m[-1] == ss:
                flag = False
                x.add(m[:-1])
            else:
                y.add(m + ss)
        if flag:
            q |= y
        q |= x
    print(len(q.pop()))


if __name__ == '__main__':
    main()
