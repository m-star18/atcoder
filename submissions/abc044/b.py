import sys
read = sys.stdin.buffer.read

from collections import Counter

print('Yes' if all(v % 2 == 0 for v in Counter(read().rstrip().decode()).values()) else 'No')
