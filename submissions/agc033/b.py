h, w, n = map(int, input().split())
ar, ac = map(int, input().split())
s = input()
t = input()
r = ac
l = ac
u = ar
d = ar
ans = False

for i in range(n):
    if s[i] == "R":
        r += 1
    if s[i] == "L":
        l -= 1
    if s[i] == "U":
        u -= 1
    if s[i] == "D":
        d += 1
    if l==0 or r==w+1 or u==0 or d==h+1:
        print("NO")
        ans = True
        break
        
    if t[i] == "R" and l != w:
        l += 1
    if t[i] == "L" and r != 1:
        r -= 1
    if t[i] == "U" and d != 1:
        d -= 1
    if t[i] == "D" and u != h:
        u += 1
 
if ans != True:
    print("YES")
