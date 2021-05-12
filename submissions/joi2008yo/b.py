import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
check = [s[i:i + 3] for i in range(len(s) - 2)]
joi, ioi = 0, 0
for ss in check:
    if ss == 'JOI':
        joi += 1
    elif ss == 'IOI':
        ioi += 1
print(joi)
print(ioi)
