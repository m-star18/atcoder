import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(read())
cnt = 0
for i in range(1, n + 1):
    if len(str(i)) % 2 == 1:
        cnt += 1
print(cnt)
