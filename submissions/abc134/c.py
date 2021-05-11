import sys
input = sys.stdin.readline

n = int(input())
a = [0]*n
for i in range(n):
    a[i] = int(input())
new_a = sorted(a)
max_a = max(new_a)
cheak = a.index(max_a)
for i in range(n):
    if i != cheak:
        print(max_a)
    else:
        print(new_a[n-2])
