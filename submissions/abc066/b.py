import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = read().rstrip().decode()
for check in range(len(s) - 2, -1, -2):
    if s[check // 2:check] == s[:check // 2]:
        print(check)
        exit()
