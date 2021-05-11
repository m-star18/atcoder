# sys.stdin.readline()
import sys
input = sys.stdin.readline

n = int(input())
c = [0]*n
for i in range(n):
    a, b = map(int, input().split())
    a = int(a/2)
    c[i] = min(a, b)
print(sum(c))
