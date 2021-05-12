import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = input()
cnt = 0
for i in range(len(s) // 2):
    if s[i] != s[-(i + 1)]:
        cnt += 1
print(cnt)
