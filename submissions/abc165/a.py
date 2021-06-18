def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    k = int(readline())
    a, b = map(int, readline().split())
    for i in range(a, b + 1):
        if i % k == 0:
            print('OK')
            break
    else:
        print('NG')


if __name__ == '__main__':
    main()
