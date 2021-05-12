import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

s = list(readline().rstrip().decode())
counter = Counter(s).values()
cnt = 0
sum_s = sum(counter)
for check in counter:
    if check % 2 == 1:
        cnt += 1
if cnt == 0:
    print(sum_s)
else:
    print((sum_s - cnt) // (cnt * 2) * 2 + 1)
