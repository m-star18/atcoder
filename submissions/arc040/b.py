import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, r = map(int, readline().split())
s = list(readline().rstrip().decode())[::-1]
for i in range(n):
    if s[i] == '.':
        check = n - (i + r)
        s = s[::-1]
        ans = 1
        for j in range(check):
            if s[j] == '.':
                for k in range(j, min(j + r, n)):
                    s[k] = 'o'
                ans += 1
            ans += 1
        print(ans)
        exit()
print(0)
