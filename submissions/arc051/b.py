import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
f = [0, 1]
for i in range(n):
    f.append(f[i] + f[i + 1])
print(f[-2], f[-1])
