import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
ans = 0
memo = {}
for i in range(1, n + 1):
    i = str(i)
    if (i[-1], i[0]) not in memo:
        memo[(i[-1], i[0])] = 1
    else:
        memo[(i[-1], i[0])] += 1
for i in range(1, n + 1):
    i = str(i)
    if (i[0], i[-1]) in memo:
        ans += memo[(i[0], i[-1])]
print(ans)
