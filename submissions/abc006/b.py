import sys
input = sys.stdin.readline

n = int(input())
ar = [0]*1000000
ar[2] = 1
for i in range(n-3):
    ar[i+3] = ar[i+2] + ar[i+1] + ar[i]
    ar[i+3] %= 10007
print(ar[n-1])
