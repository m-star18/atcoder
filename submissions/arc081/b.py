import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
s1 = readline().rstrip().decode()
s2 = readline().rstrip().decode()
mod = 10 ** 9 + 7

if s1[0] == s2[0]:
    ans = 3
    cnt = 1
else:
    cnt = 2
    ans = 6

for i in range(n):
    if cnt >= n:
        break
    if s1[cnt] != s2[cnt]:
        if s1[cnt - 1] == s2[cnt - 1]:
            ans *= 2
        else:
            ans *= 3
        cnt += 2
    else:
        if s1[cnt - 1] != s2[cnt - 1]:
            ans *= 1
        else:
            ans *= 2
        cnt += 1
    ans %= mod
print(ans)
