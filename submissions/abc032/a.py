import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
n = int(input())
ans = 0

while 1:
    if n % a == 0 and n % b == 0:
        ans = n
        break
    else:
        n += 1

print(ans)
