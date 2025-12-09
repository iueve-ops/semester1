import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def mnk(x,y):
    if len(x) != len(y):
        return 0
    x_s = sum(x) / len(x)
    y_s = sum(y) / len(y)
    x_kv_s = sum(x**2) / len(x)
    x_y = []
    for i in range (len(x)):
        x_y.append(x[i] * y[i])
    x_y_s = sum(x_y) / len(x_y)

    k = (x_y_s - x_s * y_s) / (x_kv_s - x_s**2)

    b = y_s - k * x_s

    return k, b
