# sys.stdin.readline()
import sys
input = sys.stdin.readline
import math

txa, tya, txb, tyb, t, v = map(int, input().split())
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if math.sqrt((x-txa)**2+(y-tya)**2)+math.sqrt((txb-x)**2+(tyb-y)**2) <= t*v:
        print('YES')
        sys.exit()
print('NO')
