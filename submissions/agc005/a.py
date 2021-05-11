import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

x = read().rstrip().decode()[::-1]
p = 0
m = 0
for xx in x:
    if xx == 'S' and m != 0:
        m -= 1
        p += 1
    if xx == 'T':
        m += 1
print(len(x) - 2 * p)
