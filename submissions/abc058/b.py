o = input()
e = input()
ans = ''
for i in range(len(e)):
    ans += o[i]
    ans += e[i]
if len(o)-len(e) == 1:
    ans += o[-1]
print(ans)
