import numpy as np

# vr = np.linspace(1, 100, 5,dtype=int)
# vr = np.arange(1, 10, 5, dtype=float)
# vr = np.logspace(10, 20, 5, dtype=int)
# vr = np.zeros((3, 3))
# vr = np.ones((3, 3))
# value = 5
# vr = np.full((3, 3), value)
vr = np.eye(3)

# reflections of vr and the id is different
# vrs = vr.view()

# copy of vr and the id is Same
vrs = vr

print(id(vr))
print(id(vrs))
