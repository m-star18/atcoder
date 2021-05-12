def main():
    import sys
    readline = sys.stdin.buffer.readline
    sys.setrecursionlimit(10 ** 7)

    from collections import Counter

    n = int(readline())
    s = [readline().rstrip().decode() for _ in range(n)]
    counter = Counter(s)
    print('AC x {}'.format(counter['AC']))
    print('WA x {}'.format(counter['WA']))
    print('TLE x {}'.format(counter['TLE']))
    print('RE x {}'.format(counter['RE']))


if __name__ == '__main__':
    main()
