import sys
input = sys.stdin.readline

n, l = map(int, input().split())
sum = 0
ans = [0]*n
apple = [0]*n
for i in range(n):
    apple[i] = l+i
    sum += apple[i]
    ans[i] = abs(apple[i])
print(sum-apple[ans.index(min(ans))])
