# sys.stdin.readline()
import sys
input = sys.stdin.readline

ax, ay, bx, by, cx, cy = map(int, input().split())
ans = abs((ax-cx)*(by-cy)-(bx-cx)*(ay-cy))*0.5
print(ans)
