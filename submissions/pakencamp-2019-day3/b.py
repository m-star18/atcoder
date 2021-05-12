def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    n = int(readline())
    s = [readline().rstrip().decode() for _ in range(n)]
    if s.count('black') < s.count('white'):
        print('white')
    else:
        print('black')


if __name__ == '__main__':
    main()
