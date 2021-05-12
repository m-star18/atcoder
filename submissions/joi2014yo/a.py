import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

cnt = 0
for i in range(5):
    cnt += max(40, int(readline()))
print(cnt // 5)
