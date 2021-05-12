import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h = int(readline())
cnt = 0
if h == 1:
    print(1)
elif h == 2:
    print(3)
else:
    for i in range(h):
        if h < 2 ** i:
            print(cnt)
            exit()
        else:
            cnt += 2 ** i
