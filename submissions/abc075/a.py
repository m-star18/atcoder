# sys.stdin.readline()
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
if a == b:
    print(c)
elif a == c:
    print(b)
else:
    print(a)
