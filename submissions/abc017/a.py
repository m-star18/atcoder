import sys
input = sys.stdin.readline

s_1, e_1 = map(int, input().split())
s_2, e_2 = map(int, input().split())
s_3, e_3 = map(int, input().split())

ans = (s_1 * e_1 + s_2 * e_2 + s_3 * e_3) * 0.1
print(int(ans))
