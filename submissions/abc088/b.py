import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
cnt_a = 0
cnt_b = 0
for i in range(n):
    if i%2 == 0:
        cnt_a += a[i]
    else:
        cnt_b += a[i]
print(cnt_a-cnt_b)
