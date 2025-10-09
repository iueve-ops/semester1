import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris_data.csv')

pupu = ['SepalLengthCm', 'SepalWidthCm' , 'PetalLengthCm', 'PetalWidthCm']
m = []

for i in range (len(pupu)):
    for g in range(i+1,len(pupu)):
        m.append([pupu[i], pupu[g]])
print(m)


def mnk(x,y):
    if len(x) != len(y):
        return 0
    x_s = sum(x) / len(x)
    y_s = sum(y) / len(y)
    x_kv_s = x**2 / len(x)
    x_y = []
    for i in range (len(x)):
        x_y.append(x[i] * y[i])
    x_y_s = sum(x_y) / len(x_y)

    k = (x_y_s - x_s * y_s) / (x_kv_s - x_s**2)

    b = y_s - k * x_s

    return k, b





for i in range(len(m)):
    for species, group in df.groupby("Species"):
        x = group[m[i][0]].values
        y = group[m[i][1]].values
        plt.scatter(x, y, label=species)  # для цвета

        plt.xlabel(m[i][0])
        plt.ylabel(m[i][1])
    aprx = df[m[i][0]].values
    apry = df[m[i][1]].values


    k, b = mnk(aprx, apry)

    x_queen = sum(aprx) / len(aprx)

    y_aprox = k * aprx + b
    k, b = np.polyfit(aprx, apry, 1) # y = kx + b
    y_queen = k * aprx + b
    plt.plot(aprx, y_queen, color='r')

    plt.legend() 
    plt.show()


    #plt.scatter(x, y, color='pink')
    #plt.xlabel(m[i][0])
    #.ylabel(m[i][1])
#plt.show()





