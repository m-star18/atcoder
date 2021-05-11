import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())
ab = int(str(a)+str(b))
if math.sqrt(ab).is_integer():
    ans = "Yes"
else:
    ans = "No"
print(ans)
