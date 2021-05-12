import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
n = int(readline())
lr = [list(map(int, readline().split())) for i in range(n)]
for l, r in lr:
    s = s[:l - 1] + s[l - 1:r][::-1] + s[r:]
print(s)
