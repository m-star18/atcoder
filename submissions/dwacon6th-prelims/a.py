import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
st = [readline().rstrip().decode().split() for _ in range(n)]
x = readline().rstrip().decode()
cnt = 0
flag = False
for s, t in st:
    if flag:
        cnt += int(t)
    if x == s:
        flag = True
print(cnt)
