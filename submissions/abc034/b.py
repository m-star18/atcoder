import sys
input = sys.stdin.readline

n = int(input())
if n % 2 == 0:
    ans = n - 1
else:
    ans = n + 1
print(ans)
