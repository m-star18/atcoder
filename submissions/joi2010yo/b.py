import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
x = [int(readline()) for _ in range(n)]
j = [int(readline()) for _ in range(m)]
ans = 0
cnt = 1
for check in j:
    cnt += check
    ans += 1
    if cnt >= n:
        print(ans)
        exit()
    cnt += x[cnt - 1]
    if cnt >= n:
        print(ans)
        exit()
