import sys
input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))
ans = []
sum_w = sum(w)
Cumulative_sum = w[0]
for i in range(1, n-1):
    Cumulative_sum += w[i]
    ans.append(abs(sum_w-2*Cumulative_sum))
print(min(ans))
