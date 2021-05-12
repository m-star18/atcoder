import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
check = readline().rstrip().decode()
cnt = 0
for i in range(n):
    flag = False
    s = readline().rstrip().decode()
    memo = []
    for j, ss in enumerate(s):
        if ss == check[0]:
            memo.append(j)
    for index in memo:
        for j, ss in enumerate(s[index:]):
            if ss == check[1]:
                if check == s[index:index + len(check) * j:j]:
                    flag = True
                    break
    if flag:
        cnt += 1
print(cnt)
