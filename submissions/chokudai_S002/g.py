# sys.stdin.readline()
import sys
input = sys.stdin.readline

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    c = a % b
    return gcd(b, c)

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(gcd(a, b))
