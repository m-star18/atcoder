def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    s = readline().rstrip().decode()
    if s.isupper():
        print('A')
    else:
        print('a')


if __name__ == '__main__':
    main()
