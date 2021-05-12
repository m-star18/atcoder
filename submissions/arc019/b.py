def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    a = readline().rstrip().decode()
    ans = 25 * len(a)
    flag = 2
    for bf, af in zip(a, a[::-1]):
        if bf != af:
            flag -= 1
    if len(a) % 2 == 1 and flag == 2:
        ans -= 25
    if flag == 0:
        ans -= 2
    print(ans)


if __name__ == '__main__':
    main()
