import sys
input = sys.stdin.readline

n, q = map(int, input().split())
s = input()
memo = [0] * n
cnt = 0

for i in range(1, n):
    if s[i - 1] == 'A' and s[i] == 'C':
        cnt += 1
    memo[i] = cnt

for i in range(q):
    l, r = map(int, input().split())
    print(memo[r - 1] - memo[l - 1])
