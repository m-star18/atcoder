import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
sum = 0
l.sort()
for i in range(n):
    sum += l[2*i]
print(sum)
