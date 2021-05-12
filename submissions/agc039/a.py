import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = list(readline().rstrip().decode())
k = int(read())
if len(set(s)) == 1:
    print(len(s) * k // 2)
    exit()
ans = 0
memo = 0
flag = True
for i, (bf, af) in enumerate(zip(s, s[1:])):
    if s[0] == af and flag:
        memo += 1
    else:
        flag = False
    if bf == af:
        ans += 1
        s[i + 1] = '?'
ans *= k
if s[-1] == s[0] and memo % 2 == 0:
    ans += k - 1
print(ans)
