import sys
input = sys.stdin.readline

x = int(input())
for i in range(1, 178):
    if i**4 == x:
        print(i)
        sys.exit()
