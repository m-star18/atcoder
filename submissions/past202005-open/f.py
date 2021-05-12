import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = [readline().rstrip().decode() for _ in range(n)]
ans = ''
for bf, af in zip(a[:n // 2 + n % 2], a[::-1]):
    af = list(af)
    for b in bf:
        if b in af:
            ans += b
            break
    else:
        print(-1)
        break
else:
    print(ans + ans[::-1][n % 2:])
