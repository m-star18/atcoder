import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
dict = []
memo = ''
flag = False
for i in range(len(s)):
    if flag:
        if s[i] != ' ' and s[i] != '@':
            memo += s[i]
        else:
            flag = False
            dict.append(memo)
            memo = ''
    if s[i] == '@':
        flag = True
dict.append(memo)
dict = sorted(list(set(dict)))
for ans in dict:
    if ans != '':
        print(ans)
