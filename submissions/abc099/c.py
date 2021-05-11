import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(read())
ans = n
for i in range(n + 1):
    cnt = 0
    v = i
    while v > 0:
        v, y = divmod(v, 6)
        cnt += y
    j = n - i
    while j > 0:
        j, y = divmod(j, 9)
        cnt += y
    if ans > cnt:
        ans = cnt
print(ans)
