n, a, b = map(int, input().split())
s = input()
cnt = 1
memo = 1
for i in range(n):
  if s[i] == 'c':
    print('No')
  else:
    if cnt <= a + b:
      if s[i] == 'b' and memo <= b:
        memo += 1
        cnt += 1
        print('Yes')
      elif s[i] == 'a':
        cnt += 1
        print('Yes')
      else:
        print('No')   
    else:
      print('No')
