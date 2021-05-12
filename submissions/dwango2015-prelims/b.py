import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
size = len(s)
cnt = 0
memo = 0
ans = 0
for i in range(size):
    if s[cnt:cnt + 2] == '25':
        memo += 1
        cnt += 2
    else:
        ans += memo * (memo + 1) // 2
        memo = 0
        cnt += 1
    if cnt >= size - 1:
        break
print(ans + memo * (memo + 1) // 2)
