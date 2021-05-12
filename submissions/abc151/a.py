import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

c = input()
al = [chr(ord('a') + i) for i in range(26)]
print(al[al.index(c) + 1])
