import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = list(input())
k = int(input())
for i in range(len(s)):
    num = (ord('z') - ord(s[i]) + 1) % 26
    if num <= k:
        k -= num
        s[i] = 'a'
s[-1] = chr((ord(s[-1]) - ord('a') + k) % 26 + ord('a'))
print(*s, sep='')
