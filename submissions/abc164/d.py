import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

s = readline().rstrip().decode()[::-1]
m = 0
d = 1
memo = [0]
for check in s:
    m += int(check) * d
    m %= 2019
    d *= 10
    d %= 2019
    memo.append(m)
counter = Counter(memo)
ans = 0
for i in range(2020):
    ans += counter[i] * (counter[i] - 1) // 2
print(ans)
