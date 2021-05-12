import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
s = readline().rstrip().decode()
if s[n // 2:] == s[:n // 2]:
    print('Yes')
else:
    print('No')
