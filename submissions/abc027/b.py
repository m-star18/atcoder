import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = 0
total = 0

if sum(a) % n != 0:
    ans = -1

else:
    ave = sum(a) // n
    for i in range(n):
        total += a[i] - ave
        if total != 0:
            ans += 1

print(ans)
