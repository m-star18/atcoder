import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
if len(a) < len(b):
    print('NO')
    exit()
a.sort(reverse=True)
b.sort(reverse=True)
for aa, bb in zip(a, b):
    if aa < bb:
        print('NO')
        exit()
print('YES')
