import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, w, k = map(int, readline().split())
a = [readline().rstrip().decode() for _ in range(h)]
cnt = 0
memo = 0
for aa in a:
    memo += 1
    low, high = -1, aa.find('#')
    if high == -1:
        continue
    ans = []
    while high != -1:
        cnt += 1
        ans += [cnt] * (high - low)
        low, high = high, aa.find('#', high + 1)
    ans += [cnt] * (w - low - 1)
    for i in range(memo):
        print(*ans)
    memo = 0
for i in range(memo):
    print(*ans)
