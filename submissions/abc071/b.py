import sys

s = list(input())
set_s = set(s)
new_s = list(set_s)
new_s.sort()
for i in range(26):
    if ord(new_s[i]) != 97+i:
        print(chr(97+i))
        sys.exit()
    if len(new_s) == i+1:
        if i == 25:
            break
        print(chr(98+i))
        sys.exit()
print('None')
