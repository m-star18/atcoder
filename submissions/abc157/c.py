import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
sc = [list(map(int, readline().split())) for _ in range(m)]
max_dig = 10 ** n
min_dig = 10 ** (n - 1)
if n == 1:
    min_dig -= 1
for dig in range(min_dig, max_dig):
    dig = str(dig)
    for s, c in sc:
        if dig[s - 1] != str(c):
            break
    else:
        print(dig)
        exit()
print(-1)
