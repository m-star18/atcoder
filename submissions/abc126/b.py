import re
import sys
input = sys.stdin.readline

s = input()
a = '[0][1-9]' if '0' in s[0] else '[1][0-2]'
b = '[0][1-9]' if '0' in s[2] else '[1][0-2]'
if re.search(b,s[2:4]):
    if re.search(a,s[0:2]):
        ans = 'AMBIGUOUS'
    else:
        ans = 'YYMM'
elif re.search(a,s[0:2]):
    ans = 'MMYY'
else:
    ans = 'NA'
print(ans)
