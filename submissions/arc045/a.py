import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode().split()
check = {'Left': '<', 'Right': '>', 'AtCoder': 'A'}
print(*(check[ss] for ss in s))
