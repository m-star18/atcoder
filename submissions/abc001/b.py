import math
import sys
input = sys.stdin.readline

m = int(input())/1000
if m < 0.1:
    ans = '00'
elif m <= 5:
    if m < 1:
        ans = '0'+str(math.floor(m*10))
    else:
        ans = str(math.floor(m*10))
elif m <= 30:
    ans = str(math.floor(m+50))
elif m <= 70:
    ans = str(math.floor((m-30)/5) + 80)
else:
    ans = '89'
print(ans)
