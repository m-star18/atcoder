import sys
from itertools import product
input = sys.stdin.readline

n = int(input())
ans = product("abc", repeat=n)
for i in ans:
    print("".join(i))
