import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

k = int(readline())
s = read().rstrip().decode()
if len(s) <= k:
    print(s)
else:
    print(s[:k] + '...')
