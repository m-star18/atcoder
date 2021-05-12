import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

cc = list(read().rstrip().decode())
if cc[0].lower() == cc[2]:
    print('Yes')
else:
    print('No')
