import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

deg, dis = map(int, readline().split())
h = ['NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N']
f_l = [0, 3, 16, 34, 55, 80, 108, 139, 172, 208, 245, 285, 327]
f_h = [x - 1 for x in f_l[1:]] + [10 ** 18]
deg /= 10
dis = (dis + 3) // 6
deg -= 11.25
deg //= 22.5
if deg < 0 or deg >= 15:
    h_ans = h[-1]
else:
    h_ans = h[int(deg)]
f_ans = 0
for i, (l, r) in enumerate(zip(f_l, f_h)):
    if l <= dis <= r:
        f_ans = i
if f_ans == 0:
    h_ans = 'C'
print(h_ans, f_ans)
