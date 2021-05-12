import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
k = int(input())
p = list(map(int, input().split()))
check = len(p) + 2
p += [a, b]

if len(set(p)) == check:
    ans = 'YES'
else:
    ans = 'NO'

print(ans)
