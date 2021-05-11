import sys
import re

s = input()
check = len(s)
if ('A' in s[0]) and ('C' in s[2:len(s)-1]):
    if s.count('C') == 1:
        next_s = s.replace('C', '', 1)
        if next_s[1:len(next_s)].islower():
            print('AC')
            sys.exit()
print('WA')
