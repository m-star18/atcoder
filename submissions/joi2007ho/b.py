import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
a = [int(readline()) for _ in range(k)]
a.sort()
cnt = 1
ans = 0
if a[0] == 0:
    cnt += 1
    a.pop(0)
    cnt1 = None
    for i in range(k - 2):
        if a[i] + 1 == a[i + 1]:
            cnt += 1
            if cnt1:
                cnt1 += 1
        else:
            if cnt1:
                if ans < cnt1:
                    ans = cnt1
                cnt1 = None
            if a[i] + 2 == a[i + 1]:
                cnt1 = cnt + 1
            if ans < cnt:
                ans = cnt
            cnt = 2
    if not cnt1:
        cnt1 = 0
    ans = max(ans, cnt, cnt1)
else:
    for i in range(k - 1):
        if a[i] + 1 == a[i + 1]:
            cnt += 1
        else:
            if ans < cnt:
                ans = cnt
            cnt = 1
    ans = max(ans, cnt)
print(ans)
