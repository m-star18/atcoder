import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
n = str(n)[::-1]
g = 0
k = 0
for i in range(len(n)):
    if i % 2 == 1:
        g += int(n[i])
    else:
        k += int(n[i])
print(g, k)
