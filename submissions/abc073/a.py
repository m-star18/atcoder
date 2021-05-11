# sys.stdin.readline()
import sys
input = sys.stdin.readline

n = input()
if n.count('9') == 0:
    ans = 'No'
else:
    ans = 'Yes'
print(ans)
