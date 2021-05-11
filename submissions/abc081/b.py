import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
cnt = 0

for i in range(10 ** 5):
    for j in range(len(a)):
        if a[j] % 2 != 0:
            print(cnt)
            exit()
        else:
            a[j] /= 2
    cnt += 1
