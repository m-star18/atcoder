import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import deque

q = int(readline())
s = deque()
dict = {i: 0 for i in 'abcdefghijklmnopqrstuvwxyz'}
for _ in range(q):
    qq = list(readline().rstrip().decode().split())
    if qq[0] == '1':
        s.append((qq[1], int(qq[2])))
    else:
        cnt = 0
        ans = 0
        qq[1] = int(qq[1])
        if len(s):
            while cnt + s[0][1] < qq[1]:
                dict[s[0][0]] += s[0][1]
                cnt += s[0][1]
                s.popleft()
                if len(s) == 0:
                    break
            if len(s):
                y, x = s.popleft()
                memo = qq[1] - cnt
                dict[y] += memo
                x -= memo
                s.appendleft((y, x))
        for v in dict:
            ans += dict[v] ** 2
            dict[v] = 0
        print(ans)
