def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    a, v = map(int, readline().split())
    b, w = map(int, readline().split())
    t = int(readline())
    b -= a
    b = abs(b)
    print('YES' if t * v >= t * w + b else 'NO')


if __name__ == '__main__':
    main()
