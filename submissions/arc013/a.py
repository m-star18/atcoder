import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m, l, p, q, r = map(int, read().split())
np, nq, nr = n // p, n // q, n // r
mp, mq, mr = m // p, m // q, m // r
lp, lq, lr = l // p, l // q, l // r
print(max(np * max(mq * lr, mr * lq), nq * max(mp * lr, mr * lp), nr * max(mp * lq, mq * lp)))
