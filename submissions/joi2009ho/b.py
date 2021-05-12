import sys
import bisect
input = sys.stdin.readline

D = int(input())
n = int(input())
m = int(input())
d = [0] * n
for i in range(1, n):
    d[i] = int(input())
k = [0] * m
for i in range(m):
    k[i] = int(input())
d.sort()
d.append(D)
cnt = 0
for i in range(m):
    insert_index_l = bisect.bisect_left(d, k[i])  # 昇順
    cnt += min(abs(d[insert_index_l] - k[i]), abs(k[i] - d[insert_index_l - 1]))

print(cnt)
