import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = read().rstrip().decode()
memo = []
index = 0
flag = False
for i, ss in enumerate(s):
    if ss.isupper():
        if flag:
            key = s[index:i + 1]
            memo.append([key, key.upper()])
            flag = False
        else:
            index = i
            flag = True
ans = ''
for ss, _ in sorted(memo, key=lambda x: x[1]):
    ans += ss
print(ans)
