import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    sum_a = sum(list(map(int, str(i))))
    if a <= sum_a <= b:
        cnt += i
print(cnt)
