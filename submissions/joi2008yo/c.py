import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from bisect import bisect_left

n = int(readline())
t = sorted([int(readline()) for _ in range(n)])
h = []
for i in range(1, 2 * n + 1):
    if i not in t:
        h.append(i)
flag = True
check = t.pop(0)
while t and h:
    if flag:
        index = bisect_left(h, check)
        if index != len(h):
            check = h.pop(index)
            flag = False
        else:
            check = t.pop(0)
    else:
        index = bisect_left(t, check)
        if index != len(t):
            check = t.pop(index)
            flag = True
        else:
            check = h.pop(0)
print('{0}\n{1}'.format(len(h), len(t)))
