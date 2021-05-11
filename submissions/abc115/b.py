n = int(input())
p = [int(input()) for _ in range(n)]

p[p.index(max(p))] /= 2
print(int(sum(p)))
