# sys.stdin.readline()
import sys
import math
input = sys.stdin.readline

x, y = input().split()
hex_x = int(x, 16)
hex_y = int(y, 16)
if hex_x > hex_y:
    ans = '>'
elif hex_x < hex_y:
    ans = '<'
else:
    ans = '='
print(ans)
