import sys
input = sys.stdin.readline

n = int(input())
a = [0]*n
for i in range(n):
    a[i] = int(input())
check = a[0]
for i in range(1, 10**5):
    if check == 2:
        print(i)
        sys.exit()
    else:
        check = a[check-1]
print(-1)
