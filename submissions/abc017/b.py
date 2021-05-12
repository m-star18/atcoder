import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

x = input()
cnt = 0
check = ['o', 'k', 'u']
for i in range(len(x)):
    if x[cnt] in check:
        cnt += 1
    elif x[cnt:cnt + 2] == 'ch':
        cnt += 2
    else:
        print('NO')
        exit()
    if cnt == len(x) - 1:
        break
print('YES')
