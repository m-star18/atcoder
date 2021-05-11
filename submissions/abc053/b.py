import sys
input = sys.stdin.readline

s = input()
print(s.rfind('Z')-s.find('A')+1)
