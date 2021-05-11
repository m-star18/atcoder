from collections import Counter

n = int(input())
s = [""]*n
for i in range(n):
    s[i] = input()
m = int(input())
t = [""]*m
for i in range(m):
    t[i] = input()
cnt_s = Counter(s)
cnt_t = Counter(t)
ans = [0]
cnt = 0
for i in range(len(cnt_s)):
    s_value = cnt_s.most_common()[i][0]
    s_count = cnt_s.most_common()[i][1]
    for j in range(len(cnt_t)):
        t_value = cnt_t.most_common()[j][0]
        t_count = cnt_t.most_common()[j][1]
        if s_value == t_value:
            ans.append(s_count-t_count)
            cnt = 1
            break
    if cnt == 0:
        ans.append(s_count)
    cnt = 0
print(max(ans))
