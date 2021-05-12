import sys
import math
input = sys.stdin.readline

l_oa, l_ab, l_bc = map(int, input().split())
ans = (l_oa + l_ab + l_bc) ** 2 * math.pi
if l_oa > l_ab + l_bc:
    ans -= (l_oa - l_ab - l_bc) ** 2 * math.pi
elif l_bc > l_oa + l_ab:
    ans -= (l_bc - l_oa - l_ab) ** 2 * math.pi
elif l_ab > l_oa + l_bc:
    ans -= (l_ab - l_bc - l_oa) ** 2 * math.pi
print(ans)
