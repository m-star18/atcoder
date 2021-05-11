import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import defaultdict
from bisect import bisect_left

s = readline().rstrip().decode()
t = readline().rstrip().decode()
al = defaultdict(list)
for i, ss in enumerate(s):
    al[ss].append(i + 1)
cnt = 0
tmp = 0
memo = 0
for tt in t:
    memo = bisect_left(al[tt], tmp + 1)
    if not al[tt]:
        print(-1)
        exit()
    if memo == len(al[tt]):
        memo = 0
        cnt += len(s)
    cnt += al[tt][memo] - tmp
    tmp = al[tt][memo]
print(cnt)
