import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())
b -= 1
ans = math.ceil(b / (a - 1))
print(ans)
