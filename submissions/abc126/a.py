import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = input()
if 'A' in s[k-1]:
    char = 'a'
elif 'B' in s[k-1]:
    char = 'b'
else:
    char = 'c'
ans = s[:k-1]+char+s[k:]
print(ans)
