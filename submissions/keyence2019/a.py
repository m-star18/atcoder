import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

s = readline().rstrip().decode()
check = ['1', '4', '7', '9']
counter = list(Counter(list(s)))
for k in counter:
    if k in check:
        check.pop(check.index(k))
if check:
    print('NO')
else:
    print('YES')
