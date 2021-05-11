x = input()
s = input()

answer = ''
for i in range(len(s)):
    if x not in s[i]:
        answer += s[i]
print(answer)
