import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = read().rstrip().decode()
check = s[0]
cnt = 1
ans = ''
for i in range(1, len(s)):
    if check == s[i]:
        cnt += 1
    else:
        ans += check + str(cnt)
        check = s[i]
        cnt = 1
print(ans + check + str(cnt))
