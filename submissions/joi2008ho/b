import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().strip()
t = readline().strip()
size_s = len(s)
size_t = len(t)
ans = 0
for i in range(size_t):
    index_s = 0
    index_t = i
    cnt = 0
    while index_s < size_s and index_t < size_t:
        if s[index_s] == t[index_t]:
            cnt += 1
        else:
            if ans < cnt:
                ans = cnt
            cnt = 0
        index_s += 1
        index_t += 1
    if ans < cnt:
        ans = cnt
for i in range(size_s):
    index_s = i
    index_t = 0
    cnt = 0
    while index_s < size_s and index_t < size_t:
        if s[index_s] == t[index_t]:
            cnt += 1
        else:
            if ans < cnt:
                ans = cnt
            cnt = 0
        index_s += 1
        index_t += 1
    if ans < cnt:
        ans = cnt
print(ans)
