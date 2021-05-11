# sys.stdin.readline()
import sys
input = sys.stdin.readline

r, d, x = map(int, input().split())
for i in range(10):
    new_x = r*x - d
    print(new_x)
    x = new_x
