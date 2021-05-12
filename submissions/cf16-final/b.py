import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
ans = []
cnt = 0
for i in range(1, n + 2):
    cnt += i
    ans.append(i)
    if cnt > n:
        ans.remove(cnt - n)
        break
print('\n'.join(map(str, ans)))
