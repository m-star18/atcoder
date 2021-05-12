import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = input()
k = int(input())
ans = []
for i in range(1, k + 1):
    memo = []
    for j in range(len(s) - i + 1):
        memo.append(s[j:j + i])
    ans += list(set(memo))
print(sorted(ans)[k - 1])
