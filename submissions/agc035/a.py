import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
for af in a[1:]:
    a[0] ^= af
print('Yes' if a[0] == 0 else 'No')
