import sys
input = sys.stdin.readline

r, C = map(int, input().split())
ys, xs = map(int, input().split())
yg, xg = map(int, input().split())
c = [0] * r

for i in range(r):
    c[i] = input()
n = [(ys - 1, xs - 1)]
route = {n[0]: 0}
p = [[1, 0], [0, 1], [-1, 0], [0, -1]]
count = 1

while route.get((yg - 1, xg - 1), 0) == 0 and count != 10000:
    n2 = []
    for i in n:
        for j in p:
            np = (i[0] + j[0], i[1] + j[1])
            if c[np[0]][np[1]] == '.' and route.get(np, -1) == -1:
                n2.append(np)
                route[np] = count
    n = n2
    count += 1
print(count - 1)
