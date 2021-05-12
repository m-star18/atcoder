import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = read().rstrip().decode()
cnt = 0
if s == '{}':
    print('dict')
    exit()
ans = False
for ss in s[1:]:
    if ss == '{':
        cnt += 1
    elif ss == '}':
        cnt -= 1
    elif ss == ':' and cnt == 0:
        ans = True
        break
print('dict' if ans else 'set')
