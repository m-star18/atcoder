import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
w = list(readline().rstrip().decode().split())
check = [('z', 'r'), ('b', 'c'), ('d', 'w'), ('t', 'j'), ('f', 'q'), ('l', 'v'), ('s', 'x'), ('p', 'm'), ('h', 'k'), ('n', 'g')]
ans = []
for ww in w:
    ww = ww.lower()
    memo = ''
    for m in ww:
        for i, num in enumerate(check):
            if m in num:
                memo += str(i)
                break
    if memo != '':
        ans.append(memo)
print(' '.join(ans))
