import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = [int(readline()) for _ in range(n)]
if a[0] != 0:
    print(-1)
    exit()
ans = 0
for ab, af in zip(a, a[1:]):
    if af - ab > 1:
        print(-1)
        exit()
    if ab >= af:
        ans += af
    else:
        ans += 1
print(ans)
