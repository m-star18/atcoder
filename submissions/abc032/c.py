import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k, *s = map(int, read().split())
if 0 in s:
    print(n)
    exit()
s += [float('inf')]
index = 0
ans = 0
v = 1
for i, (bf, af) in enumerate(zip(s, s[1:])):
    v *= bf
    for _ in range(index, i + 1):
        if v <= k:
            break
        v //= s[index]
        index += 1
    ans = max(ans, i + 1 - index)
print(max(ans, n - index))
