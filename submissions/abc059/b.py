import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
if a > b:
    ans = 'GREATER'
elif a < b:
    ans = 'LESS'
else:
    ans = 'EQUAL'
print(ans)
