import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
s = read().rstrip().decode()
ans = n - 1
for bf, af in zip(s, s[1:]):
    if bf != af:
        ans -= 1
print(min(n - 1, ans + k * 2))
