import sys
read = sys.stdin.buffer.read
readline = sys.stdin.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
m = int(readline())
k = [int(readline()) for _ in range(m)]
ans = [(i + 1) for i in range(2 * n)]
for check in k:
    if check == 0:
        a = ans[:n]
        b = ans[n:]
        ans = []
        for i in range(2 * n):
            if i % 2 == 0:
                ans.append(a[i // 2])
            else:
                ans.append(b[i // 2])
    else:
        ans = ans[check:] + ans[:check]
print('\n'.join(map(str, ans)))
