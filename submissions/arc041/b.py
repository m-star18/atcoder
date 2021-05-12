import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
b = [list(map(int, list(readline().rstrip().decode()))) for _ in range(n)]
print('0' * m)
for i in range(1, n - 1):
    ans = '0'
    for j in range(1, m - 1):
        check = min(b[i + 1][j], b[i - 1][j], b[i][j + 1], b[i][j - 1])
        ans += str(check)
        b[i + 1][j] -= check
        b[i - 1][j] -= check
        b[i][j + 1] -= check
        b[i][j - 1] -= check
    print(ans + '0')
print('0' * m)
