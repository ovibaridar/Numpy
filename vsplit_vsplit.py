import numpy as np

vr = np.arange(1, 10, 1).reshape(3, 3)
print("Original Array:\n", vr)


arr = np.vsplit(vr,3)
print("\nArray after split:\n", arr)

arr = np.hsplit(vr,3)
print("\nArray after split:\n", arr)
