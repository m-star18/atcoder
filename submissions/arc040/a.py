import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
s = read().rstrip().decode()
r = s.count('R')
b = s.count('B')
if r > b:
    print('TAKAHASHI')
elif r == b:
    print('DRAW')
else:
    print('AOKI')
