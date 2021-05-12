import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
t = readline().rstrip().decode()
if s == t:
    print('same')
elif s.upper() == t.upper():
    print('case-insensitive')
else:
    print('different')
