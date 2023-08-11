import numpy as np
vr = np.array([[1, 1, 2, 3], [3, 4, 4, 5]])
vrs = np.array([[12, 12, 22, 32], [32, 42, 42, 52]])
print(vr, "\n")
print(vrs, "\n")
stack = np.stack((vr, vrs), axis=0)
print(stack, "stack col \n")
stack = np.stack((vr, vrs), axis=1)
print(stack, "stack row\n")
