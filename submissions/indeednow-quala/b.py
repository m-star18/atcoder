import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
indeed = list('indeednow')
indeed.sort()
check_indeed = list(Counter(indeed).items())
flg = True
for i in range(n):
    flg = True
    s = list(input().rstrip('\n'))
    s.sort()
    check_s = list(Counter(s).items())
    if len(check_s) != len(check_indeed):
        flg = False
    else:
        for j in range(len(check_indeed)):
            if check_indeed[j][0] == check_s[j][0] and check_indeed[j][1] == check_s[j][1]:
                flg = True
            else:
                flg = False
                break
    if flg:
        print('YES')
    else:
        print('NO')
