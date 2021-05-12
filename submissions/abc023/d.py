import sys
input = sys.stdin.readline


def check(n):
    memo = []
    for h, s in hs:
        if h > n:
            return False
        memo.append((n - h) / s)
    memo.sort()
    return all(i <= t for i, t in enumerate(memo))


n = int(input())
hs = [list(map(int, input().split())) for i in range(n)]
min_value = 0
max_value = 10 ** 15

while max_value - min_value > 1:
        mid = (max_value + min_value) // 2
        if check(mid):
            max_value = mid
        else:
            min_value = mid

print(max_value)
