import sys
import math
input = sys.stdin.readline

x = int(input())
memo = math.floor(x / 500)
ans = memo * 1000 + math.floor((x - memo * 500) / 5) * 5
print(ans)
