import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
q = int(readline())
r = list(range(n))
c = list(range(n))
flag = False

for _ in range(q):
    q = readline().rstrip().decode()
    if q[0] == '3':
        r, c = c, r
        flag = not flag
    else:
        f, a, b = q.split()
        a = int(a) - 1
        b = int(b) - 1
        if f == '1':
            r[a], r[b] = r[b], r[a]
        elif f == '2':
            c[a], c[b] = c[b], c[a]
        else:
            a = r[a]
            b = c[b]
            if flag:
                a, b = b, a
            print(a * n + b)
