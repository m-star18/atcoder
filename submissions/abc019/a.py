import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
age = [a, b, c]
age.sort()
print(age[1])
