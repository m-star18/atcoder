import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
if len(s) % 2 == 1:
    print('No')
    exit()
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] != 'h':
            print('No')
            exit()
    else:
        if s[i] != 'i':
            print('No')
            exit()
print('Yes')
