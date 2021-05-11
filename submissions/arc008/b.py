import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter
from math import ceil

n, m = map(int, readline().split())
name = list(Counter(list(readline().rstrip().decode())).items())
kit = list(Counter(list(readline().rstrip().decode())).items())
ans = 0
for check, cnt in name:
    flag = True
    for k, v in kit:
        if check == k:
            flag = False
            ans = max(ans, ceil(cnt / v))
            break
    if flag:
        print(-1)
        exit()
print(ans)
