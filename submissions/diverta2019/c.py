import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
cnt_a = 0
cnt_b = 0
cnt_c = 0
cnt = 0
for i in range(n):
    s = input()
    for j in range(1, len(s)):
        if s[j - 1] == 'A' and s[j] == 'B':
            cnt += 1
    if s[0] == 'B' and s[-1] == 'A':
        cnt_c += 1
    elif s[0] == 'B':
        cnt_b += 1
    elif s[-1] == 'A':
        cnt_a += 1
ans = cnt
if cnt_c == 0:
    ans += min(cnt_a, cnt_b)
else:
    if cnt_a + cnt_b > 0:
        ans += cnt_c + min(cnt_a, cnt_b)
    else:
        ans += cnt_c - 1
print(ans)

