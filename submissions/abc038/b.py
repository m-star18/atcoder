import sys
input = sys.stdin.readline

h_1, w_1 = map(int, input().split())
h_2, w_2 = map(int, input().split())

if h_1 == h_2 or h_1 == w_2 or w_1 == h_2 or w_1 == w_2:
    ans = 'YES'
else:
    ans = 'NO'

print(ans)
