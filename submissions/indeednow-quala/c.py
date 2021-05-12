import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
s = sorted([int(readline()) for _ in range(n)], reverse=True)
q = int(readline())
k = [int(readline()) for _ in range(q)]
cnt = s.count(0)
for qq in k:
    if n - cnt <= qq:
        print(0)
    else:
        print(s[qq] + 1)
