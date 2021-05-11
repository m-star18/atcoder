k = int(input())

if (k%2) == 0:
    ans = int((k*0.5)**2)
else:
    ans = int((k*0.5-0.5) * (k*0.5+0.5))
print(ans)
