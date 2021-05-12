import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
ans = [0]
for check in range(max(0, n - 153), n):
    cnt = check
    check = str(check)
    for i in range(len(check)):
        cnt += int(check[i])
    if cnt == n:
        ans[0] += 1
        ans.append(check)
for a in ans:
    print(a)
