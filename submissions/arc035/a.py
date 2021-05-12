import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
for bf, af in zip(s, s[::-1]):
    if bf != af and bf != '*' and af != '*':
        print('NO')
        break
else:
    print('YES')
