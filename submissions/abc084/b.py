a, b = map(int, input().split())
s = input()
new_s = s[:a]+s[a+1:]
if len(s) == a+b+1:
    if "-" in s[a]:
        for i in new_s:
            if "-" in i:
                print("No")
                exit()
        print("Yes")
        exit()
print("No")
