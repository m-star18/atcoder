import sys
input = sys.stdin.readline

x, y = map(int, input().split())

if x < y:
    ans = 'Better'
else:
    ans = 'Worse'

print(ans)
