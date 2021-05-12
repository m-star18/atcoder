import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
s = input()
t = input()
for i in range(n):
    if s[i:] == t[:n - i]:
        print(n + i)
        exit()
print(n * 2)
