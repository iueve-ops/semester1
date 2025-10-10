import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0,1,2,3,4]
y = [0, 2, 4, 6, 8]


x_app = [0,4]
y_app = [i*2 for i in x_app]

plt.scatter(x, y)
plt.plot(x_app, y_app)
plt.grid()
plt.show()
