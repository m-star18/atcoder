import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
for i in range(1, 11):
    if 20 * i >= n:
        if i % 2 == 1:
            print(n - 20 * (i - 1))
            exit()
        else:
            print(20 * i - n + 1)
            exit()
