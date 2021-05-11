N = int(input())
A = [int (input()) for i in range(5)]

m = min(A)

if m == 1:
    times = 5 + (N - 1)
else:
    times = 5 + (N // m)

print(times)
