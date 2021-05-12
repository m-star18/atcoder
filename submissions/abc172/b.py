def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    s = readline().rstrip().decode()
    t = readline().rstrip().decode()
    cnt = 0
    for ss, tt in zip(s, t):
        if ss != tt:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
