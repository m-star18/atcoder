import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = list(readline().rstrip().decode())
b = list(readline().rstrip().decode())
c = list(readline().rstrip().decode())
cnt = 0
for aa, bb, cc in zip(a, b, c):
    if aa == bb == cc:
        continue
    elif aa == bb or bb == cc or aa == cc:
        cnt += 1
    else:
        cnt += 2
print(cnt)
