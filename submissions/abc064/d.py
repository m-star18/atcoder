n = int(input())
s = input()
cnt = 0
cnt_start = 0
for i in range(n):
    if '(' in s[n-i-1]:
        if cnt > 0:
            cnt -= 1
        else:
            cnt_start += 1
    else:
        cnt += 1
for i in range(cnt_start):
    s = s+')'
for j in range(cnt):
    s = '('+s
print(s)
