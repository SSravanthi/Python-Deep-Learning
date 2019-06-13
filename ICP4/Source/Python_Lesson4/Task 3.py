# Support Vector Machine  Classification Using Linear and RBF Kernel
# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pandas as pd

# Importing the dataset

dataset = pd.read_csv('glass.csv')

# looking at the values of the dataset

dataset.head()

# Spliting the dataset in independent and dependent variables

X = dataset.values  # taking features for prediction
#print(X)
Y = dataset['Type'].values


# Splitting the dataset into the Training set and Test set

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)


# Fitting SVC Classification to the Training set with linear kernel

svc_linear = SVC(kernel='linear', C=1, gamma=0.1).fit(X_train, y_train)


# Accuracy of SVM Linear kernel on Training set

print('Accuracy of the SVM Linear Kernel Classification on training part is: ', svc_linear.score(X_train, y_train))


# Accuracy of SVM Linear Kernel on Test Set

print('Accuracy of the SVM Linear Kernel Classification on testing part is: ', svc_linear.score(X_test, y_test))


