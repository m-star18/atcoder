import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

abc = list(map(int, readline().split()))
if abc.count(1) < abc.count(2):
    print(2)
else:
    print(1)
