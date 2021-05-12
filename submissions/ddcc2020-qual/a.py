import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

check = list(map(int, readline().split()))
prize = [3 * 10 ** 5, 2 * 10 ** 5, 10 ** 5]
ans = 0
if check.count(1) == 2:
    ans = 10 ** 6
else:
    if check[0] <= 3:
        ans += prize[check[0] - 1]
    if check[1] <= 3:
        ans += prize[check[1] - 1]
print(ans)
