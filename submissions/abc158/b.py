import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, a, b = map(int, readline().split())
if n <= a + b:
    print(min(n, a))
else:
    ans = n // (a + b) * a
    if n % (a + b) < a:
        ans += n % (a + b)
    else:
        ans += a
    print(ans)
