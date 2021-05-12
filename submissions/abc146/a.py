import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = input()
ans = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
print(7 - ans.index(s))
