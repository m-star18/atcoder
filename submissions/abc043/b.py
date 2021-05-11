import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = read().rstrip().decode()
ans = ''
for ss in s:
    if ss == 'B':
        if ans:
            ans = ans[:-1]
    else:
        ans += ss
print(ans)
