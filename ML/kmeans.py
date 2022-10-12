import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from sklearn import metrics
from sklearn.cluster import KMeans
names=['sepal-length','sepal-width','petal-length','petal-width','Species']

dataset=pd.read_csv("iris.data",names=names)
dataset.head()

x=dataset.iloc[:,0:4].values

kmeans =KMeans(n_clusters=3,random_state=0).fit(x)
print('the four cluster centers are : ',kmeans.cluster_centers_)
print('lables of each data point ', kmeans.labels_)

plt.scatter(x[:,0], x[:,1])
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c="green")
plt.xlabel("petal-length")
plt.ylabel("petal-width")
plt.show()
