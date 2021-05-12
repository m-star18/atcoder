import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(read())
for i in range(1, 3501):
    for h in range(i, 3501):
        check = 4 * i * h - n * (i + h)
        if check > 0:
            v = n * i * h
            if v % check == 0:
                print(i, h, v // check)
                exit()
