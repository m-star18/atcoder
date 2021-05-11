import sys
input = sys.stdin.readline

n = int(input())
d, x = map(int, input().split())
cnt = x+n
for i in range(n):
    a = int(input())
    cnt += (d-1)//a
print(cnt)
