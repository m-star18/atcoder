import sys
input = sys.stdin.readline

s = input()
for i in range(len(s)):
    if s[i] in s[:i]:
        print('no')
        sys.exit()
print('yes')
