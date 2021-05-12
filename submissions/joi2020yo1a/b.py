import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
s = readline().rstrip().decode()
print(s.count('a') + s.count('i') + s.count('u') + s.count('e') + s.count('o'))
