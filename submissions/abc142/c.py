import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
memo = [[0, 0] for i in range(n)]
for i, j in enumerate(a):
    memo[i][0] = j
    memo[i][1] = i + 1
memo.sort()
for i in range(n):
    print(memo[i][1], end=' ')
print()
