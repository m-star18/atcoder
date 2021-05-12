import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
x = [input() for i in range(n)]
cnt = 0
flag = False
for i in range(9):
    for j in range(n):
        if x[j][i] == 'o':
            flag = True
        else:
            if x[j][i] == 'x':
                cnt += 1
            if flag:
                cnt += 1
                flag = False
    if flag:
        cnt += 1
        flag = False
print(cnt)
