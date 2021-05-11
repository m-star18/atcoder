# sys.stdin.readline()
import sys
import math
input = sys.stdin.readline

a = input()
b = input()
if (a[0] in b[2]) and (a[1] in b[1]) and (a[2] in b[0]):
    ans = 'YES'
else:
    ans = 'NO'
print(ans)
