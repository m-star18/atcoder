import sys
input = sys.stdin.readline

s = input()
t = input()
check = ['a', 't', 'c', 'o', 'd', 'e', 'r']
for i in range(len(s)):
    if s[i] in t[i]:
        pass
    elif ('@' in s[i]) and (t[i] in check):
        pass
    elif ('@' in t[i]) and (s[i] in check):
        pass
    else:
        print('You will lose')
        sys.exit()
print('You can win')
