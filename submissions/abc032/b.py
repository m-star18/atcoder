import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = input()
k = int(input())
check = set()
for i in range(len(s) - k + 1):
    check.add(s[i:i + k])
print(len(check))
