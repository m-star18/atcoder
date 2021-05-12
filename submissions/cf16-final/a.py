import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, w = map(int, readline().split())
s = [readline().rstrip().decode().split() for _ in range(h)]
al = [chr(ord('A') + i) for i in range(26)]
for i in range(h):
    for j in range(w):
        if s[i][j] == 'snuke':
            print(al[j] + str(i + 1))
