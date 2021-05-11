import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = list(map(int, readline().split()))
cnt = 0
for aa in a:
    for i in range(aa):
        if aa % 2 == 0:
            cnt += 1
            aa //= 2
        else:
            break
print(cnt)
