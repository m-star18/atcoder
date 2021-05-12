import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
p = list(map(int, readline().split()))
q = list(map(int, readline().split()))
ans = [''] * 10
for i in range(n):
    ans[p[i]] = '.'
for i in range(m):
    ans[q[i]] = 'o'
for i in range(10):
    if ans[i] == '':
        ans[i] = 'x'
print(ans[7], ans[8], ans[9], ans[0])
print(' ' + ans[4], ans[5], ans[6])
print('  ' + ans[2], ans[3])
print('   ' + ans[1])
