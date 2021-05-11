import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = read().rstrip().decode() + '+'
cnt = 0
flag = 2
for i in range(1, len(s) + 1, 2):
    if s[i] == '+':
        if flag != 1 and s[i - 1] != '0':
            cnt += 1
        flag = 2
    else:
        if flag == 2:
            flag = 0
        if flag == 0 and s[i - 1] == '0':
            flag = 1
print(cnt)
