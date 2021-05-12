import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = input()
cnt = 0
ans = 0
size = len(s)
flag = False
for i in range(size):
    if cnt >= size - i:
        flag = True
    if s[i] == 'p':
        cnt -= 1
    if s[i] == 'g':
        if flag:
            ans += 1
        else:
            cnt += 1
if flag:
    print(ans)
else:
    print(min(cnt, 0))
