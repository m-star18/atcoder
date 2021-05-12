import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
al = [chr(ord('A') + i) for i in range(26)] * 2
al = al[::-1]
ans = ''
for check in s:
    index = al.index(check)
    ans += al[index + 3]
print(ans)
