import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
a, b, c, d = map(int, read().split())
print(s[:a] + '"' + s[a:b] + '"' + s[b:c] + '"' + s[c:d] + '"' + s[d:])
