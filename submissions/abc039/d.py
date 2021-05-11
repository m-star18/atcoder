import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, w = map(int, readline().split())
s = [readline().rstrip().decode() for _ in range(h)]


def check(i, j, m, flag):
    if m[i][j] == flag:
        return False
    if i != 0 and j != 0:
        if m[i - 1][j - 1] == flag:
            return False
    if i != 0 and j != w - 1:
        if m[i - 1][j + 1] == flag:
            return False
    if i != h - 1 and j != 0:
        if m[i + 1][j - 1] == flag:
            return False
    if i != h - 1 and j != w - 1:
        if m[i + 1][j + 1] == flag:
            return False
    if i != 0:
        if m[i - 1][j] == flag:
            return False
    if j != 0:
        if m[i][j - 1] == flag:
            return False
    if i != h - 1:
        if m[i + 1][j] == flag:
            return False
    if j != w - 1:
        if m[i][j + 1] == flag:
            return False
    return True


ans = []
for i in range(h):
    memo = ''
    for j in range(w):
        if check(i, j, s, flag='.'):
            memo += '#'
        else:
            memo += '.'
    ans.append(memo)
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            if check(i, j, ans, flag='#'):
                print('impossible')
                exit()
print('possible')
print('\n'.join(ans))
