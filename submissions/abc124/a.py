a, b = map(int, input().split())

ans = max((a+a-1),(a+b),(b+b-1))
print(ans)
