import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
ans = max(a)-min(a)
print(ans)
