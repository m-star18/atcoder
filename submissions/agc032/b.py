import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
graph = []
for i in range(1, n):
    for j in range(i + 1, n + 1):
        graph.append([i, j])
if n % 2 == 0:
    for i in range(n // 2):
        graph.remove([i + 1, n - i])
else:
    for i in range(n // 2):
        graph.remove([i + 1, n - i - 1])
print(len(graph))
for ans in graph:
    print(*ans)
