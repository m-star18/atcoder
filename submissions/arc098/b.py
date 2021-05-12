import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = list(map(int, readline().split()))
ans = n
index = 0
v = 0
for i, (bf, af) in enumerate(zip(a, a[1:])):
    v += bf
    for _ in range(index, i + 1):
        if v ^ af == v + af:
            break
        v -= a[index]
        index += 1
    ans += i + 1 - index
print(ans)
