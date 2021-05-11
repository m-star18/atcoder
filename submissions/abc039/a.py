import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
ans = 2*a*b + 2*b*c + 2*a*c
print(ans)
