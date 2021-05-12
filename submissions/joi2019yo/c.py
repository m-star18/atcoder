import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
s = readline().rstrip().decode()
index = 0
cnt = 0
for i in range(n):
    if index + 1 >= n:
        break
    if s[index: index + 2] == 'OX' or s[index: index + 2] == 'XO':
        cnt += 1
        index += 2
    else:
        index += 1
print(cnt)
