A,B,C= map(int, input().split())

cut = B // A
if cut >= C:
    ans = C
else:
    ans = cut
print(ans)
