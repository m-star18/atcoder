import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, a, b = map(int, readline().split())
a -= 1
s = readline().rstrip().decode()
print(s[:a] + s[a:b][::-1] + s[b:])
