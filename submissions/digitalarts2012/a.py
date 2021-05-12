import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = list(readline().rstrip().decode().split())
n = int(readline())
t = [readline().rstrip().decode() for _ in range(n)]
ans = []
for check in s:
    for ng in t:
        if len(check) == len(ng):
            for i in range(len(ng)):
                if '*' != ng[i] != check[i]:
                    break
            else:
                ans.append('*' * len(check))
                break
    else:
        ans.append(check)
print(*ans)
