a, op, b = input().split()
a = int(a)
b = int(b)
if "+" in op:
    ans = a + b
else:
    ans = a - b
print(ans)
