import sys

s = input()
t = input()
check = []
check.append(t[len(t)-1]+t[0:len(t)-1])
for i in range(1, len(t)+1):
    check.append(check[i-1][len(t)-1]+check[i-1][0:len(t)-1])
    if s == check[i-1]:
        print('Yes')
        sys.exit()
print('No')
