import numpy as nm

ar1 = nm.array([1, 2, 3, 4])
ar2 = nm.array([5, 2, 3, 4])

if ar1.size == ar2.size:
    if nm.all(ar1 == ar2):
        print("ok")
    else:
        print("no")
        ar3 = nm.where(ar1 % 2 != 0, ar1, 0)
        print(ar3)

else:
    print("array is not equal")
