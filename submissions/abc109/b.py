import sys
input = sys.stdin.readline

n = int(input())
w = [''] * n
for i in range(n):
    w[i] = input().rstrip('\n')
for i in range(1, n):
    if w[i - 1][-1] != w[i][0]:
        print('No')
        exit()
if len(set(w)) == len(w):
    print('Yes')
else:
    print('No')
