import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
s_dict = {}
for i in range(n):
    s = ''.join(sorted(input()))
    if s not in s_dict:
        s_dict[s] = 0
    else:
        s_dict[s] += 1
        cnt += s_dict[s]
print(cnt)
