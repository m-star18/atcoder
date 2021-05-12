import sys
input = sys.stdin.readline

n = int(input())
for i in range(10, 10 ** 4 + 1):
    memo = 0
    i = str(i)
    for j in range(len(i)):
        if j == 0:
            memo += int(i[-1])
        else:
            memo += int(i) ** j * int(i[-(j + 1)])
    if memo == n:
        print(i)
        exit()
print(-1)
