import sys
input = sys.stdin.readline

n = int(input())
t = [0]*n
for i in range(n):
    t[i] = int(input())
print(min(t))
