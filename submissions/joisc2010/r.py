import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
ans = ''
now = 2 ** n
for i in range(n):
    now //= 2
    if now >= k:
        ans += ("J" * now + "O" * now)
        print(ans)
        exit()
    else:
        ans += "I" * now
        k -= now
print(ans + 'J')
