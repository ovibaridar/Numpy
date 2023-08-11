import numpy as np
vr = np.array([[1, 1, 2, 3], [3, 4, 4, 5]])
vrs = np.array([[12, 12, 22, 32], [32, 42, 42, 52]])
print(vr, "\n")
print(vrs, "\n")
concat = np.concatenate((vr, vrs), axis=0)
print(concat, "\n")
concat = np.concatenate((vr, vrs), axis=1)
print(concat, "\n")
