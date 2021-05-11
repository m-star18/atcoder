import sys
input = sys.stdin.readline

a, b = input().split()
if 'H' in a:
    if 'H' in b:
        ans = 'H'
    else:
        ans = 'D'
else:
    if 'H' in b:
        ans = 'D'
    else:
        ans = 'H'
print(ans)
