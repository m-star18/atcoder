import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from itertools import accumulate

n = int(readline())
a = list(map(int, readline().split()))
cumsum = list(accumulate(a[::-1]))
ans = 0
check = 1
for aa, v in zip(a, cumsum[::-1]):
    if aa > check:
        print(-1)
        exit()
    else:
        ans += min(check, v)
        check -= aa
        check *= 2
print(ans)
