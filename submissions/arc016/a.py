import sys
input = sys.stdin.readline

n, m = map(int, input().split())
if m == 1:
    print(m + 1)
else:
    print(m - 1)
