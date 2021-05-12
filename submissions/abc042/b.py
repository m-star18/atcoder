import sys
input = sys.stdin.readline

n, l = map(int, input().split())
s = [''] * n
ans = ''
for i in range(n):
    s[i] = input()
s.sort()
for i in range(n):
    ans += s[i].rstrip('\n')
print(ans)
