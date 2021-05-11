import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
cnt = 0
q = ['3', '5', '7']
while q:
    qq = q.pop()
    v = list(qq)
    if '3' in v and '5' in v and '7' in v:
        cnt += 1
    if int(qq + '3') <= n:
        q.append(qq + '3')
        if int(qq + '5') <= n:
            q.append(qq + '5')
            if int(qq + '7') <= n:
                q.append(qq + '7')
print(cnt)
