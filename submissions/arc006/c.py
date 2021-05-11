import sys
input = sys.stdin.readline

n = int(input())
w = [0] * n
ans = 0
cnt = 0
for i in range(n):
    w[i] = int(input())

for i in range(n):
    ans += 1
    memo = 0
    cnt = w.pop(memo)

    for j in range(len(w)):
        if cnt >= w[memo]:
            cnt = w.pop(memo)
        else:
            memo += 1

        if len(w) - memo == 0:
            break

    if len(w) == 0:
        break

print(ans)
