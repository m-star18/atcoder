import sys
input = sys.stdin.readline

w, h, x, y = map(int, input().split())
ans = (w*h)/2
if x == w/2 and y == h/2:
    max = 1
else:
    max = 0
print(ans, max)
