import sys
input = sys.stdin.readline

n = int(input())
ans = 800*n - 200*(n//15)
print(ans)
