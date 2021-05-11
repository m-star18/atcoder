# sys.stdin.readline()
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if (a+b)%3 == 0 or a%3 == 0 or b%3 == 0:
    ans = 'Possible'
else:
    ans = 'Impossible'
print(ans)
