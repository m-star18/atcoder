import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

ab = readline().rstrip().decode()
if ' ' in ab:
    _, b = map(int, ab.split())
else:
    b = int(readline())
a = list(map(int, readline().split()))
bb = list(map(int, readline().split())) + [0]
ans = 0
for i in range(b):
    cnt = 0
    for aa in a:
        if aa == bb[i + cnt]:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
