import sys
input = sys.stdin.readline

n = int(input())
sum = 0
for i in range(1, n+1):
    sum += 10000*i
print(sum//n)
