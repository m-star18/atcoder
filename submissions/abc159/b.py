s = input()
len_s = len(s)
for i in range(len_s):
    if s[i] != s[len_s - i - 1]:
        print('No')
        exit()
for i in range((len_s - 1) // 2):
    if s[i] != s[(len_s - 1) // 2 - 1 - i] or s[(len_s + 2) // 2 + i] != s[(len_s - 1) - i]:
        print('No')
        exit()
print('Yes')
