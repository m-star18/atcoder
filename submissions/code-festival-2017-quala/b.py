import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
for i in range(n + 1):
    for j in range(m + 1):
        if k == (n - i) * j + (m - j) * i:
            print('Yes')
            exit()
print('No')
