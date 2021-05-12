import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, c = map(int, readline().split())
a = [int(readline()) for _ in range(n)]
ans = float('inf')
for i in range(1, 11):
    for j in range(1, 11):
        if i == j:
            continue
        memo = 0
        for k in range(n):
            if k % 2 == 0 and a[k] != i:
                memo += c
            if k % 2 == 1 and a[k] != j:
                memo += c
        ans = min(ans, memo)
print(ans)
