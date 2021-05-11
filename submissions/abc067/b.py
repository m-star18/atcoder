import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
sum = 0
for i in range(k):
    sum += l[i]
print(sum)
