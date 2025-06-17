import numpy as np

a = np.random.randint(1, 51, size=(5, 4))
print(a)
anti_diagonal = np.array([a[i, -1 - i] for i in range(min(a.shape))])
print("\nAnti-diagonal elements:", anti_diagonal)
row_max = np.max(a, axis=1)
print(row_max)
x=np.mean(a)
new_a=a[a<=x]
print(new_a)
def numpy_boundary_traversal(matrix):
  l = []
  i = 0
  j = 1
  while i < matrix.shape[1]:
    l.append(matrix[0, i])
    i += 1
  while j < matrix.shape[0]:
    l.append(matrix[j, matrix.shape[1] - 1])
    j += 1
  while (i-1) > 0:
    i -= 1
    l.append(matrix[matrix.shape[0] - 1, i-1])
  while j-1 > 1:
    j -= 1
    l.append(matrix[j-1, 0])
  t=np.array(l)
  return t
