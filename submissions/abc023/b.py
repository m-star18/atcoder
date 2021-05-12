import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
s = input()
mid = (n - 1) // 2
if n % 2 == 0:
    print(-1)
    exit()
for i in range(mid + 1):
    if i % 3 == 0:
        if s[mid + i] != 'b' or s[mid - i] != 'b':
            print(-1)
            exit()
    if i % 3 == 1:
        if s[mid + i] != 'c' or s[mid - i] != 'a':
            print(-1)
            exit()
    if i % 3 == 2:
        if s[mid + i] != 'a' or s[mid - i] != 'c':
            print(-1)
            exit()
print(mid)
