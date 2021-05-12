import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

from numpy import *

m, n = int32(readline().split())
readline()
memo = zeros((m + 1, n + 2), 'S1')
for i in range(m):
    memo[i + 1, 1:] = frombuffer(readline(), 'S1')
q = int32(read().split())
j = cumsum(cumsum(memo == b'J', 1), 0)
o = cumsum(cumsum(memo == b'O', 1), 0)
a, b, c, d = q[::4] - 1, q[1::4] - 1, q[2::4], q[3::4]
j = j[a, b] + j[c, d] - j[a, d] - j[c, b]
o = o[a, b] + o[c, d] - o[a, d] - o[c, b]
i = (c - a) * (d - b) - j - o
print('\n'.join('%d %d %d' % i for i in zip(j, o, i)))
