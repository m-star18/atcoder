import sys
input = sys.stdin.readline

n = int(input())
ng = [0]*3
for i in range(3):
    ng[i] = int(input())
if n in ng:
    print('NO')
    sys.exit()
for i in range(100):
    for j in range(3, 0, -1):
        if n-j not in ng:
            n -= j
            break
    if n <= 0:
        print('YES')
        sys.exit()
if n <= 0:
    ans = 'YES'
else:
    ans = 'NO'
print(ans)
