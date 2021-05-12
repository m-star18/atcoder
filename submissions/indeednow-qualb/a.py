import sys
input = sys.stdin.readline

x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())
ans = abs(x_1 - x_2) + abs(y_1 - y_2) + 1
print(ans)
