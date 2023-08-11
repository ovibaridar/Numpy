import numpy as np

# vr = np.linspace(1, 100, 5, dtype=int)
# vr = np.arange(1, 10, 5, dtype=float)
# vr = np.logspace(10, 20, 5, dtype=int)
# vr = np.zeros((3, 3))
# vr = np.ones((3, 3))
# value = 5
# vr = np.full((3, 3), value)
vr = np.arange(1, 10, 1)

# reflections of vr and the id is different
# vrs = vr.view()

# copy of vr and the id is Same
# vrs = vr
print(id(vr))

# vrs = vr.view()
# print(vrs)
# print(id(vrs))
# vrs[3] = 400
# print(vrs, "vrs after change")
# print(vr, "vr after change")

# vrs = vr.copy()
# print(vrs)
# print(id(vrs))
# vrs[3] = 400
# print(vrs, "vrs after change")
# print(vr, "vr after change")
