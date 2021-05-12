import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, r, n = map(int, readline().split())
if r == 1:
    print(a)
    exit()
for _ in range(n):
    if a > 10 ** 9:
        print('large')
        break
    a *= r
else:
    print(a // r)
