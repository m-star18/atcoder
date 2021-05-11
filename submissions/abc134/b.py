import sys
import math
input = sys.stdin.readline

n, d = map(int, input().split())
ans = n/(d*2+1)
ans = math.ceil(ans)
print(ans)
