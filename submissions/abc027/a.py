import sys
input = sys.stdin.readline

i_1, i_2, i_3 = map(int, input().split())

if i_1 != i_2 and i_2 == i_3:
    ans = i_1

elif i_2 != i_1 and i_1 == i_3:
    ans = i_2

elif i_3 != i_1 and i_1 == i_2:
    ans = i_3

else:
    ans = i_1

print(ans)
