import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
t = read().rstrip().decode()
print('Yes' if s == t[:-1] else 'No')
