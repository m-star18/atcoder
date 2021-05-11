import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
s = readline().rstrip().decode()
cumsum = []
check = []
flag = True
for i in range(n):
    if s[i] == '0':
        if flag:
            cumsum.append(i)
        flag = False
    else:
        if not flag:
            check.append(i)
        flag = True
if not flag:
    check.append(n)
cumsum.append(n)
if len(cumsum) - 1 <= k:
    print(n)
else:
    ans = cumsum[k]
    for i in range(k, len(cumsum) - 1):
        ans = max(ans, cumsum[i + 1] - check[i - k])
    print(ans)
