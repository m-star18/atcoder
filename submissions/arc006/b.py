import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, l = map(int, readline().split())
a = [readline().rstrip().decode() for _ in range(l)][::-1]
check = list(readline().rstrip().decode()).index('o')
for i in range(l):
    if check > 0:
        if a[i][check - 1] == '-':
            check -= 2
            continue
    if check < 2 * (n - 1):
        if a[i][check + 1] == '-':
            check += 2
print(check // 2 + 1)
