import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = list(read().rstrip().decode()[::-1])
ans = ''
for i, (bf, af) in enumerate(zip(s, s[1:])):
    if bf == 'A' and af == 'W':
        s[i + 1] = 'A'
        ans = 'C' + ans
    else:
        ans = bf + ans
print(s[-1] + ans)
