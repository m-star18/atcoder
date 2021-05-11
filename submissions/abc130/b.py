import sys
input = sys.stdin.readline

n, x = map(int, input().split())
l = list(map(int, input().split()))
sum = 0
for i in range(n):
    sum += l[i]
    if sum > x:
        print(i+1)
        sys.exit()
print(n+1)
