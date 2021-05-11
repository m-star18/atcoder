# sys.stdin.readline()
import sys
import math
input = sys.stdin.readline

n = input()
if '000' in n or '111' in n or '222' in n or '333' in n or '444' in n or '555' in n or '666' in n or '777' in n or '888' in n or '999' in n:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
