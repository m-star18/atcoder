import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
s = read().rstrip().decode()
cnt = 0
for i in range(1000):
    num = str(i).zfill(3)
    idx = -1
    for m in num:
        idx = s.find(m, idx + 1)
        if idx == -1:
            break
    else:
        cnt += 1
print(cnt)
