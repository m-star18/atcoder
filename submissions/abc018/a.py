import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
point = [a, b, c]
rank = sorted(point, reverse=True)

for i in range(3):
    print(rank.index(point[i]) + 1)
