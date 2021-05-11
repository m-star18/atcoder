import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
if s[0] == s[1]:
    print(1, 2)
    exit()
for i, (af, s, bf) in enumerate(zip(s, s[1:], s[2:])):
    if af == s or af == bf or s == bf:
        print(i + 1, i + 3)
        exit()
print(-1, -1)
