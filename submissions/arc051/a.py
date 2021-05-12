import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

x_1, y_1, r = map(int, readline().split())
x_2, y_2, x_3, y_3 = map(int, readline().split())
if x_2 <= x_1 - r and y_2 <= y_1 - r and x_1 + r <= x_3 and y_1 + r <= y_3:
    print('NO')
    print('YES')
    exit()
r **= 2
if (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 <= r and (x_1 - x_3) ** 2 + (y_1 - y_3) ** 2 <= r and (x_1 - x_3) ** 2 + (y_1 - y_2) ** 2 <= r and (x_1 - x_2) ** 2 + (y_1 - y_3) ** 2 <= r:
    print('YES')
    print('NO')
else:
    print('YES')
    print('YES')
