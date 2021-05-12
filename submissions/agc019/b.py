import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a = read().rstrip().decode()
al = [chr(ord('a') + i) for i in range(26)]
ans = len(a) * (len(a) - 1) // 2 + 1
for check in al:
    cnt = a.count(check)
    ans -= cnt * (cnt - 1) // 2
print(ans)
