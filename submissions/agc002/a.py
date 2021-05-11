import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if a <= 0:
    if b >= 0:
        ans = 'Zero'
    elif b < 0 and (b-a)%2 == 0:
        ans = 'Negative'
    else:
        ans = 'Positive'
else:
    ans = 'Positive'
print(ans)
