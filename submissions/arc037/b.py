import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from scipy.sparse import *
import numpy as np

n, m = map(int, readline().split())
memo = np.array([readline().split() for _ in range(m)], dtype=np.int64)
memo -= 1
graph = csr_matrix((np.ones(m), (memo[:, 0], memo[:, 1])), (n, n))
_, labels = csgraph.connected_components(graph)

cnt = max(labels)
print((np.bincount(labels, minlength=cnt + 1) == np.bincount(labels[memo[:, 0]], minlength=cnt + 1) + 1).sum())
