import sys
input = sys.stdin.readline

n, a, b, c, d = map(int, input().split())
s = input()
if '##' in s[a:c-1] or '##' in s[b:d-1]:
    ans = 'No'
elif c > d:
    if '...' in s[b-2:d+1]:
        ans = 'Yes'
    else:
        ans = 'No'
else:
    ans = 'Yes'
print(ans)
