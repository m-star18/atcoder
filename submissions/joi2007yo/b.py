import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = [int(readline()) for _ in range(28)]
for check in range(1, 31):
    if check not in s:
        print(check)
