import math

n = int(input())
n_check = n
num = []
for i in range(int(math.log10(n)+1)+1):
    num.append(n % 10)
    n /= 10
    n -= num[i]/10
if n_check%int(sum(num)) == 0:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
