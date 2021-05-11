import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

c_1 = list(map(int, readline().split()))
c_2 = list(map(int, readline().split()))
c_3 = list(map(int, readline().split()))
c = [c_1, c_2, c_3]
a = [min(c_1), min(c_2), min(c_3)]
b = [c_1[0] - a[0], c_2[1] - a[1], c_3[2] - a[2]]
for i in range(3):
    for j in range(3):
        if a[i] + b[j] != c[i][j]:
            print('No')
            exit()
print('Yes')
