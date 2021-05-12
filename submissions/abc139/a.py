import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
t = readline().rstrip().decode()
cnt = 0
for i in range(3):
    if s[i] == t[i]:
        cnt += 1
print(cnt)
