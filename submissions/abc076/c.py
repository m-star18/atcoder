import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
t = read().rstrip().decode()
ans = []
for i in range(len(s) - len(t) + 1):
    for j, (ss, tt) in enumerate(zip(s[i:], t)):
        if ss not in ('?', tt):
            break
    else:
        memo = s[:i] + t + s[i + len(t):]
        ans.append(memo.replace('?', 'a'))
print(min(ans) if ans else 'UNRESTORABLE')
