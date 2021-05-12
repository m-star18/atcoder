import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
a = [int(readline()) for _ in range(m)][::-1]
ans = set()
size = 0
for aa in a:
    ans.add(aa)
    if len(ans) != size:
        print(aa)
        size += 1
ans = sorted(list(ans) + [10 ** 5 + 1])
cnt = 0
for i in range(1, n + 1):
    if i == ans[cnt]:
        cnt += 1
    else:
        print(i)
