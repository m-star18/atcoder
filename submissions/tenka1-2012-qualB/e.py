import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b, c = map(int, readline().split())
for i in range(1, 128):
    if i % 3 == a and i % 5 == b and i % 7 == c:
        print(i)
