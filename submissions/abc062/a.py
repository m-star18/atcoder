import sys
input = sys.stdin.readline

x, y = map(int, input().split())
gloup_a = [1, 3, 5, 7, 8, 10, 12]
gloup_b = [4, 6, 9, 11]
gloup_c = [2]
if ((x in gloup_a) and (y in gloup_a)) or ((x in gloup_b) and (y in gloup_b)) or ((x in gloup_c) and (y in gloup_c)):
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
