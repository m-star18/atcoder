import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

c = read().rstrip().decode()
ans = ''
flag = False
for check in c:
    if check != ' ':
        if flag:
            ans += ','
            flag = False
        ans += check
    else:
        flag = True
print(ans)
