# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:19:11 2021

Scikit/ sklearn - https://scikit-learn.org/stable/
SVM - Support Vector Machine
Unsupervised learning - KMeans clusters
"""

from sklearn import datasets, svm
import pylab
import numpy as np

data = datasets.load_digits()

# Let's visualize some digits
digit = data['images'][400]
pylab.imshow(digit, cmap='gray')
pylab.show()

# Let's build a "training based" classifier to classify these digits
# We split the data into two parts
# One part for training (1000); the other for testing (797)

X_train = data['data'][:1000]
Y_train = data['target'][:1000]

X_test = data['data'][1000:]
Y_test = data['target'][1000:]

clf = svm.SVC(gamma=1e-3)
clf.fit(X_train, Y_train)

predicted = clf.predict(X_test)

# In case you wish to try your own 8x8 image
img = pylab.imread('test.png')
img_int = np.round(img * 16)
#img_int = img.astype('int')
print()
print(clf.predict(img_int[:2].reshape(64,1).T))  # TO ASK: Doing slicing to make it run

print()
print('####################################################################')
print()

from sklearn.cluster import KMeans

N = 200
SIGMA = 1

X1 = np.array([1., 1.]) + SIGMA * np.random.randn(N,2)
X2 = np.array([3.5, 4.5])+ SIGMA * np.random.randn(N,2)

X = np.concatenate([X1, X2])

kmeans = KMeans(n_clusters = 2)
kmeans.fit(X)
print(kmeans.cluster_centers_)

#pylab.scatter(X[:,0], X[:,1])
# Plot with class colours
predicted_data = kmeans.predict(X)
class_1_data = X[predicted_data == 0]
class_2_data = X[predicted_data == 1]

pylab.scatter(class_1_data[:,0], class_1_data[:,1], color='r')
pylab.scatter(class_2_data[:,0], class_2_data[:,1], color='g')
pylab.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], color='k',s=100)

pylab.show()

print()
print('####################################################################')
print()




