import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b, c = map(int, readline().split())
n = int(readline())
ijkr = [list(map(int, readline().split())) for _ in range(n)]
ijkr.sort(key=lambda x: -x[3])
check = [2] * (a + b + c)
for i, j, k, r in ijkr:
    if r == 1:
        check[i - 1] = 1
        check[j - 1] = 1
        check[k - 1] = 1
    else:
        if check[i - 1] == 2 and check[j - 1] == check[k - 1] == 1:
            check[i - 1] = 0
        elif check[j - 1] == 2 and check[i - 1] == check[k - 1] == 1:
            check[j - 1] = 0
        elif check[k - 1] == 2 and check[j - 1] == check[i - 1] == 1:
            check[k - 1] = 0
print('\n'.join(map(str, check)))
