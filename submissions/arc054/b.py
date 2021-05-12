import sys
import math
input = sys.stdin.readline

p = float(input())
low = 0
high = 100000
ans = 0

if (1 - 2 * p * math.log(2) * (math.pow(2, - 2 * low / 3)) / 3) > 0:
    print(p)
    exit()

while 1:
    mid = (low + high) / 2
    y_dif = 1 - 2 * p * math.log(2) * (math.pow(2, - 2 * mid / 3)) / 3
    if abs(y_dif) < math.pow(10, -4):
        ans = mid + p / math.pow(2, mid / 1.5)
        break
    if y_dif > 0:
        high = mid
    else:
        low = mid

print(ans)
