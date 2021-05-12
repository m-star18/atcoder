import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a_1, a_2, a_3 = map(int, readline().split())
if a_1 + a_2 + a_3 >= 22:
    print('bust')
else:
    print('win')
