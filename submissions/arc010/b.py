import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
memo = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
check = []
for i in range(n):
    md = readline().rstrip().decode()
    index = md.index('/')
    check.append([int(md[:index]) - 1, int(md[index + 1:]) - 1])
sum_d = 0
cnt = 0
ans = 0
flag = 0
for m in range(12):
    for d in range(memo[m]):
        if sum_d % 7 == 6 or sum_d % 7 == 0:
            for mm, dd in check:
                if m == mm and d == dd:
                    flag += 1
            cnt += 1
        elif any(m == mm and d == dd for mm, dd in check):
            cnt += 1
        elif flag > 0:
            cnt += 1
            flag -= 1
        else:
            ans = max(ans, cnt)
            cnt = 0
        sum_d += 1
print(max(ans, cnt))
