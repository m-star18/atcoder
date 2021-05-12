import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(read())


def check(s):
    if len(s) == n:
        print(s)
    else:
        for i in range(97, ord(max(s)) + 2):
            check(s + chr(i))


check('a')
