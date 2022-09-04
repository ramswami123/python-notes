import numpy as np
import matplotlib.pyplot as plt
plt.style.use('./deeplearning.mplstyle')
# x_train is the input variable (size in 1000 square feet)
# y_train is the target (price in 1000s of dollars)
x_train = np.array([1.0, 231.0,345.0,-1.0])
y_train = np.array([300.0, 400.0])
for i in x_train:
    print(i)
print(f"x_train = {x_train}")
print("y_train = {y_train}")

#output
#1.0
#231.0
#345.0
#-1.0
#x_train = [  1. 231. 345.  -1.]
#y_train = {y_train}
