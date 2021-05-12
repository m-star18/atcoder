import sys
import collections
input = sys.stdin.readline

n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
cnt = list(collections.Counter(a).items())
ans = 0
for i in range(len(cnt)):
    ans += cnt[i][1] - 1
print(ans)
