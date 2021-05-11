import sys
input = sys.stdin.readline

e = list(map(int, input().split()))
b = int(input())
l = list(map(int, input().split()))
cnt = 0
ans = 0
for i in range(6):
    if l[i] in e:
        cnt += 1
if cnt == 6:
    ans = 1
elif cnt == 5:
    if b in l:
        ans = 2
    else:
        ans = 3
elif cnt == 4:
    ans = 4
elif cnt == 3:
    ans = 5
print(ans)
