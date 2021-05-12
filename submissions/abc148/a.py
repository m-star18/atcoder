import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a = int(readline())
b = int(readline())
ans = [1, 2, 3]
for i in ans:
    if i != a and i != b:
        print(i)
