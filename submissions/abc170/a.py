def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    x = list(map(int, readline().split()))
    for i in range(1, 6):
        if i not in x:
            print(i)
            break


if __name__ == '__main__':
    main()
