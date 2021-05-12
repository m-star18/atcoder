import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s, t = readline().rstrip().decode().split()
ans = 0
if s[0] == 'B' and t[0] == 'B':
    ans = abs(int(s[1]) - int(t[1]))
elif s[0] == 'B' and t[1] == 'F':
    ans = int(s[1]) + int(t[0]) - 1
elif s[1] == 'F' and t[0] == 'B':
    ans = int(s[0]) + int(t[1]) - 1
else:
    ans += abs(int(s[0]) - int(t[0]))
print(ans)
