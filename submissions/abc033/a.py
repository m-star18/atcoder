import sys
input = sys.stdin.readline

n = input()

if len(set(n)) == 2:
    ans = 'SAME'
else:
    ans = 'DIFFERENT'

print(ans)
