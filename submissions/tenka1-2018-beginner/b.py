import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b, k = map(int, read().split())
for i in range(k):
    if i % 2 == 0:
        if a % 2 == 1:
            a -= 1
        b += a // 2
        a //= 2
    else:
        if b % 2 == 1:
            b -= 1
        a += b // 2
        b //= 2
print(a, b)
