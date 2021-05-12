import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
c = list(map(int, readline().split()))
for check in [a, b, c]:
    if check[2] > check[5]:
        if check[4] == 0:
            check[3] -= 1
            check[4] += 59
        else:
            check[4] -= 1
        check[5] += 60
    if check[1] > check[4]:
        check[3] -= 1
        check[4] += 60
    print(check[3] - check[0], check[4] - check[1], check[5] - check[2])
