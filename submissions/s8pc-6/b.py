import sys
input = sys.stdin.readline

n = int(input())
a = [0] * n
b = [0] * n
cnt = 0
ans = [0] * n ** 2
for i in range(n):
    a[i], b[i] = map(int, input().split())

for i in range(n):
    for j in range(n):
        for k in range(n):
            if a[i] <= a[k]:
                if b[j] <= b[k]:
                    cnt += 2 * b[k] - a[i] - b[j]
                else:
                    cnt += b[j] - a[i]

            else:
                if b[j] <= b[k]:
                    cnt += a[i] - b[j] + 2 * (b[k] - a[k])
                else:
                    cnt += a[i] + b[j] - 2 * a[k]

        ans[i * n + j] = cnt
        cnt = 0

print(min(ans))
