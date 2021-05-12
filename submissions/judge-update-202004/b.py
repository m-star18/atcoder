import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
memo_r = []
memo_b = []
for i in range(n):
    x, c = input().split()
    if c == 'R':
        memo_r.append((int(x)))
    else:
        memo_b.append(int(x))
memo_r.sort()
memo_b.sort()
for r in memo_r:
    print(r)
for b in memo_b:
    print(b)
