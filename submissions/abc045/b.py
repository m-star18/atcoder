import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a = list(input())
b = list(input())
c = list(input())
game = [a, b, c]
ans = ['A', 'B', 'C']
memo = 0
for i in range(len(a) + len(b) + len(c)):
    check = game[memo].pop(0)
    if check == 'a':
        memo = 0
    elif check == 'b':
        memo = 1
    else:
        memo = 2
    if len(game[memo]) == 0:
        break
print(ans[memo])
