import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
ans = [0] * (2 ** n)
for i in range(1, n + 1):
    flag = 0
    for j in range(2 ** n):
        if ans[j] == 0:
            if flag == 0:
                x = [a[j], j]
                flag += 1
            else:
                flag = 0
                if i != n:
                    if x[0] > a[j]:
                        ans[j] = i
                    else:
                        ans[x[1]] = i
                else:
                    ans[j] = i
                    ans[x[1]] = i
print(*ans)
