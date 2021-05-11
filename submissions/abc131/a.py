import sys
input = sys.stdin.readline

s = input()
for i in range(3):
    if s[i] in s[i+1]:
        print('Bad')
        sys.exit()
print('Good')
