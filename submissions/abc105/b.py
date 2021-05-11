import sys
n = int(input())

if n%7 != 0 and n%4 != 0 and n%11 != 0:
    for a in range(1, 25):
        for b in range(1, 14):
            if n%(7*b + 4*a) == 0:
                print('Yes')
                sys.exit()
else:
    print('Yes')
    sys.exit()
print('No')
