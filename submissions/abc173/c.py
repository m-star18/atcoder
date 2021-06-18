def main():
    import sys
    readline = sys.stdin.buffer.readline
    sys.setrecursionlimit(10 ** 7)

    from itertools import product

    h, w, k = map(int, readline().split())
    c = [readline().rstrip().decode() for _ in range(h)]
    cnt = 0
    for bit_y in product([0, 1], repeat=h):
        for bit_x in product([0, 1], repeat=w):
            memo = 0
            for i, cc in enumerate(c):
                if bit_y[i] == 1:
                    continue
                for j, dc in enumerate(cc):
                    if dc == '#' and bit_x[j] == 0:
                        memo += 1
            if memo == k:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
