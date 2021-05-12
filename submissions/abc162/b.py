import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
cnt = 0
for i in range(n + 1):
    if i % 3 != 0 and i % 5 != 0:
        cnt += i
print(cnt)
