import sys
input = sys.stdin.readline

n = int(input())
for i in range(8):
    if n < 2**i:
        print(2**(i-1))
        sys.exit()
