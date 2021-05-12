import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = readline().rstrip().decode()
for bf, af in zip(n, n[::-1]):
    if bf != af:
        print('NO')
        break
else:
    print('YES')
