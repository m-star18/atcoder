import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from re import findall

s = read().rstrip().decode()
check = ['S10|SJ|SQ|SK|SA', 'H10|HJ|HQ|HK|HA', 'D10|DJ|DQ|DK|DA', 'C10|CJ|CQ|CK|CA']
ans = ''
for ss in s:
    ans += ss
    for match in check:
        m = findall(match, ans)
        if len(m) == 5:
            for mm in m:
                ans = ans.replace(mm, '')
            if len(ans) == 0:
                print(0)
            else:
                print(ans)
            exit()
