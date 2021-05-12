import sys
input = sys.stdin.readline

n = int(input())
S = []
for i in range(n):
    s = list(input().split())
    S.append(s)

for i in range(n):
    for j in range(n):
        print(S[n - 1 - j][0][i], end='')
    print()
