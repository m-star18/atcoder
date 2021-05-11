import sys
read = sys.stdin.buffer.read
readline = sys.stdin.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
memo = sum(map(int, str(n)))
cnt = memo // 9
ans = memo % 9 * (10 ** cnt) + 10 ** cnt - 1
if n == ans:
    if ans <= 10:
        print(9 + ans)
    else:
        print((memo % 9 + 1) * (10 ** cnt) + 10 ** cnt - 1 - (10 ** (cnt - 1)))
else:
    print(ans)
