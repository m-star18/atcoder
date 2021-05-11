# sys.stdin.readline()
import sys
input = sys.stdin.readline

n = int(input())
c = [0]*n
for i in range(n):
    a, b = map(int, input().split())
    c[i] = max(a, b)
print(sum(c))
