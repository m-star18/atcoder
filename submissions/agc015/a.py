import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, a, b = map(int, readline().split())
if a > b:
    print(0)
elif n == 1:
    if a != b:
        print(0)
    else:
        print(1)
else:
    print(a + b * (n - 1) - (b + a * (n - 1)) + 1)
