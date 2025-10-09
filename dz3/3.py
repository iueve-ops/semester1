import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris_data.csv')

species = df['Species'].value_counts()


setosa = species['Iris-setosa']

versicolor = species['Iris-versicolor']

virginica  = species['Iris-virginica']

plt.title('ириски')

plt.pie([setosa, versicolor, virginica], labels = ['Iris-setosa','Iris-versicolor','Iris-virginica'], colors = ['c', 'pink', 'violet'])

plt.show()


plt.title('ириски')

PetalLengthCm = df['PetalLengthCm'].value_counts()
print(PetalLengthCm)


count1 = 0
count2 = 0
count3 = 0

for i, g in PetalLengthCm.items():
    if i < 1.2:
        count1 += g
    if i > 1.2 and i < 1.5:
        count2 += g
    if i > 1.5:
        count3 += g




mini= count1

btw12and15 = count2

more15  = count3

plt.pie([mini, btw12and15, more15], labels = ['меньше 1.2см','больше 1.2см и меньше 1.5см','больше 1.5см'])

plt.title('размер ириски')

plt.show()