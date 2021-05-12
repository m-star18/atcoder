import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import deque

k = int(readline())
q = deque(list(map(str, list(range(1, 10)))))
for i in range(k - 1):
    x = q.popleft()
    y = int(x[-1])
    if y != 0:
        q.append(x + str(y - 1))
    q.append(x + x[-1])
    if y != 9:
        q.append(x + str(y + 1))
print(q[0])
