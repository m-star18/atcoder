# sys.stdin.readline()
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
print(min(a+b,a+c,b+c))
