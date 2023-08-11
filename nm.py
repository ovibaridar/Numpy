import numpy as np

# vr = np.linspace(1, 100, 5, dtype=int)
# vr = np.arange(1, 10, 5, dtype=float)
# vr = np.logspace(10, 20, 5, dtype=int)
# vr = np.zeros((3, 3))
# vr = np.ones((3, 3))
# value = 5
# vr = np.full((3, 3), value)
# vr = np.arange(1, 10, 1)

# reflections of vr and the id is different
# vrs = vr.view()

# copy of vr and the id is Same
# vrs = vr
# print(id(vr))

# vrs = vr.view()
# print(vrs)
# print(id(vrs))
# vrs[3] = 400
# print(vrs, "vrs after change")
# print(vr, "vr after change")

# vrs = vr.copy()
# print(vrs, "vrs\n")
# print(vr, "vr\n")
# print(id(vrs), "vrs\n")
# print(id(vr), "vr\n")
# vrs[2] = 200
# print(vrs, "vrs\n")
# print(vr, "vr\n")

# vr = np.array([[1, 2, 3], [3, 4, 5]])
# vrs = np.array([[12, 21, 33], [34, 45, 56]])
# print(vr)
# print(vrs)
#
# vradd = np.add(vr, vrs)
# vrasub = np.subtract(vrs, vr)
# vramultiplication = np.multiply(vrs, vr)
# vramod = np.mod(vrs, 2)
# vrareciprocal = np.reciprocal(vr)
#
#
# print("Numpy add\n", vradd)
# print("Numpy subtract\n", vrasub)
# print("Numpy multiply\n", vramultiplication)
# print("Numpy MOD\n", vramod)
# print("Numpy reciprocal\n", vrareciprocal)
