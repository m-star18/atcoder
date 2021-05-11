import sys
input = sys.stdin.readline

k, x = map(int, input().split())
ans = [x]
for i in range(1, k):
    ans.insert(0, x-i)
    ans.append(x+i)
for i in range(2*k-1):
    print(ans[i], end=' ')
