import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = list(readline().rstrip().decode())
while 1:
    for j in range(len(s)):
        if s[j] == '(':
            idx = j + 1
        if s[j] == ')':
            s = s[:idx - 1] + s[idx:j] + s[idx:j][::-1] + s[j + 1:]
            break
    else:
        break
print(*s, sep='')
