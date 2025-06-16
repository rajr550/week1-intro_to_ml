import numpy as np

a = np.random.randint(1, 51, size=(5, 4))
print(a)
anti_diagonal = [a[i, -1 - i] for i in range(min(a.shape))]
print("\nAnti-diagonal elements:", anti_diagonal)
row_max = np.max(a, axis=1)
print(row_max)
x=np.mean(a)
new_a=a[a<=x]
print(new_a)