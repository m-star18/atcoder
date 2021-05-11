import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dict = {}
for i in range(n):
    dict[a[i]] = i
for x, y in sorted(dict.items(), key=lambda x: -x[0]):
    print(y+1)
