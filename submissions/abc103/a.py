a_1, a_2, a_3 = map(int, input().split())

maxs = max(a_1, a_2, a_3)
mins = min(a_1, a_2, a_3)
ans = maxs-mins
print(ans)
