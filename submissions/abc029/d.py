import sys
input = sys.stdin.readline

n = int(input())
str_n = str(n)
cnt = 0
for i in range(len(str_n)):
    j = i+1
    cnt += (n//(10**j) * (10**i))
    if int(str_n[-j]) > 1:
        cnt += 10**i
    elif int(str_n[-j]) == 1:
        cnt += (n%(10**j)+1) - 10**i
print(cnt)
