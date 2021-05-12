import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == n:
            print('Yes')
            exit()
print('No')
