import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if a == b:
    ans = 0
elif (a+b)%2 == 0:
    ans = (a+b)//2
else:
    ans = "IMPOSSIBLE"
print(ans)
