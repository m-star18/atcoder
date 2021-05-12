import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

t = readline().rstrip().decode()
t = t.replace('?', 'D')
print(t)
