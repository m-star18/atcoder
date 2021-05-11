import sys
input = sys.stdin.readline

n = int(input())
d = [0]*n
for i in range(n):
    d[i] = int(input())
ans_d = list(set(d))
print(len(ans_d))
