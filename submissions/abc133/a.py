import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
ans = min(n*a, b)
print(ans)
