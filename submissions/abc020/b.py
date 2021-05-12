import sys
input = sys.stdin.readline

a, b = map(int, input().split())
ans = int(str(a) + str(b)) * 2
print(ans)
