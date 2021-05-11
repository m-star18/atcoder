import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if a == 1:
    a += 13
if b == 1:
    b += 13
if a > b:
    ans = "Alice"
elif a == b:
    ans = "Draw"
else:
    ans = "Bob"
print(ans)
