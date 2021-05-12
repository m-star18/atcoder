s = input()
cnt = 0
for i in range(1, len(s) + 1):
    if i % 2 == 0:
        cnt -= int(s[i - 1])
    else:
        cnt += int(s[i - 1])
print(cnt)
