import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(read())
if len(bin(n)[2:]) % 2 == 0:
    p = 0
    m = 1
else:
    p = 1
    m = 0
v = 1
for i in range(n):
    v <<= 1
    if i % 2 == 0:
        v += p
    else:
        v += m
    if v > n:
        print('Aoki' if i % 2 == 0 else 'Takahashi')
        break
