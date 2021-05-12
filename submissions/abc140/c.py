import sys
input = sys.stdin.readline

n = int(input())
b = list(map(int, input().split()))
ans = b[0]
b.append(b[-1])
for i in range(1, n):
    memo = min(b[i], b[i - 1])
    ans += memo
print(ans)
