import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

n, p = map(int, readline().split())
s = readline().rstrip().decode()
cnt = 0
if p == 2 or p == 5:
    for i, ss in enumerate(s):
        if int(ss) % p == 0:
            cnt += (i + 1)
else:
    memo = [0]
    m = 0
    d = 1
    for ss in s[::-1]:
        m += int(ss) * d
        m %= p
        d *= 10
        d %= p
        memo.append(m)
    counter = Counter(memo)
    for i in range(p + 1):
        cnt += counter[i] * (counter[i] - 1) // 2
print(cnt)
