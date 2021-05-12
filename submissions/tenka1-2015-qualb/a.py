import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a = [100, 100, 200]
for i in range(17):
    a.append(a[i] + a[i + 1] + a[i + 2])
print(a[-1])
