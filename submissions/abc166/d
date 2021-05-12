import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

x = int(readline())
for a in range(-500, 500):
    for b in range(-500, 500):
        if pow(a, 5) == x + pow(b, 5):
            print(a, b)
            exit()
