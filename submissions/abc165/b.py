def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    x = int(readline())
    v = 100
    for i in range(10 ** 6):
        if v >= x:
            print(i)
            break
        v += v // 100


if __name__ == '__main__':
    main()
