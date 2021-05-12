s = input()
S = ['AKIHABARA', 'KIHABARA', 'AKIHBARA', 'AKIHABRA', 'AKIHABAR',
     'KIHBARA', 'KIHABRA', 'KIHABAR', 'AKIHBRA', 'AKIHBAR', 'AKIHABR',
     'AKIHBR', 'KIHABR', 'KIHBAR', 'KIHBRA', 'KIHBR',
     ]

if s in S:
    ans = 'YES'
else:
    ans = 'NO'

print(ans)
