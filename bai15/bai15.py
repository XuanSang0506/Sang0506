import numpy as np
x = np.array([[14, 96],
              [np.nan, 82],
              [80, 67],
              [77, np.nan],
              [99, 87]])
print("x = ", x)
print("Range = ", np.ptp(x))
print("Range (axis = 0) = ", np.ptp(x, axis=0))
print("Range (axis = 1) = ", np.ptp(x, axis=1))