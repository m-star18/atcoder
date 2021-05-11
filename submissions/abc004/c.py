import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(read())
x, y = divmod(n % 30, 5)
ans = list(range(x + 1, 7)) + list(range(1, x + 1))
ans.insert(y, ans.pop(0))
print(*ans, sep='')
