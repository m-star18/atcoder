def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    n, m, k = map(int, readline().split())
    a = list(map(int, readline().split()))
    b = list(map(int, readline().split()))
    if n == m:
        for aa, bb in zip(a, b):
            if aa < bb:
                print('X')
                break
            elif aa > bb:
                print('Y')
                break
        else:
            print('Same')
    else:
        print('X' if n < m else 'Y')


if __name__ == '__main__':
    main()
