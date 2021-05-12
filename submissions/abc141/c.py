import sys
input = sys.stdin.readline

n, k, q = map(int, input().split())
memo = [0] * n
for i in range(q):
    a = int(input())
    memo[a - 1] += 1
for i in range(n):
    if k - (q - memo[i]) > 0:
        print('Yes')
    else:
        print('No')
