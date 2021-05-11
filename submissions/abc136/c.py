import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *h = map(int, read().split())
h = h[::-1]
for i, (bf, af) in enumerate(zip(h, h[1:])):
    if bf + 1 < af:
        print('No')
        exit()
    if bf < af:
        h[i + 1] -= 1
print('Yes')
