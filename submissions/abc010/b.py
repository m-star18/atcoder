import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(a[i]):
        if (a[i]-j)%3 == 2 or (a[i]-j)%2 == 0:
            cnt += 1
        else:
            break
print(cnt)
