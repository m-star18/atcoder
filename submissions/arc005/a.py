import sys
input = sys.stdin.readline

n = int(input())
w = list(input().split())
ans = ['TAKAHASHIKUN', 'Takahashikun', 'takahashikun']
cnt = 0
w[n - 1] = w[n - 1].rstrip('.')
for i in range(n):
    if len(w[i]) == 12 and w[i] in ans:
        cnt += 1

print(cnt)
