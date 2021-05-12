import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = read().rstrip().decode().upper()
check = ['I', 'C', 'T']
for ss in s:
    if ss in check[0]:
        check.pop(0)
    if not check:
        print('YES')
        break
else:
    print('NO')
