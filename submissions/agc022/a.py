import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode() + chr(96)
for i, ss in enumerate(s[::-1]):
    for m in range(ord(ss) + 1, 123):
        if chr(m) not in list(s[:-(i + 1)]):
            print(s[:-(i + 1)] + chr(m))
            exit()
print(-1)
