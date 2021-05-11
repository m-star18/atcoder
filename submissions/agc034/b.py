import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = '?' + read().rstrip().decode()[::-1]
ans = 0
cnt = 0
index = 0
for _ in range(len(s) + 1):
    if s[index] == 'C' and s[index + 1] == 'B':
        cnt += 1
        index += 1
    elif s[index] == 'A':
        ans += cnt
    else:
        cnt = 0
    index += 1
    if index >= len(s) - 1:
        break
if s[-1] == 'A':
    ans += cnt
print(ans)
