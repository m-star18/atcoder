s = input()

ans = s.translate(str.maketrans({'9':'1', '1':'9'}))
print(ans)
