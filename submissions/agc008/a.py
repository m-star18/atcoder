import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

x, y = map(int, readline().split())
if x <= y:
    if (x >= 0 and y >= 0) or (x <= 0 and y <= 0):
        ans = y - x
    else:
        ans = abs(abs(x) - y) + 1
else:
    if (x >= 0 and y >= 0) or (x <= 0 and y <= 0):
        ans = min(abs(x) + abs(y) + 1, abs(abs(y) - abs(x)) + 2)
    else:
        ans = abs(x - abs(y)) + 1
print(ans)
