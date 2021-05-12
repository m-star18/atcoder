import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
ps = [list(input().split()) for i in range(m)]
check = [True] * n
ac = 0
wa = [0] * n
cnt_wa = 0
for p, s in ps:
    p = int(p)
    if check[p - 1]:
        if s == 'AC':
            check[p - 1] = False
            ac += 1
        else:
            wa[p - 1] += 1
for i in range(n):
    if not check[i]:
        cnt_wa += wa[i]
print(ac, cnt_wa)
