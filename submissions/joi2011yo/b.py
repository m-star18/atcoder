import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
n = int(readline())
cnt = 0
for _ in range(n):
    check = readline().rstrip().decode() * 2
    if s in check:
        cnt += 1
print(cnt)
