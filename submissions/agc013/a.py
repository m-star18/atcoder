import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = list(map(int, readline().split()))
cnt = 1
flag = True
memo = 0
for i in range(1, n):
    if flag:
        if a[i] > a[i - 1]:
            memo = 1
            flag = False
        if a[i] < a[i - 1]:
            flag = False
            memo = 0
        else:
            continue
    else:
        if memo == 1 and a[i] < a[i - 1]:
            cnt += 1
            flag = True
        elif memo == 0 and a[i] > a[i - 1]:
            cnt += 1
            flag = True
print(cnt)
