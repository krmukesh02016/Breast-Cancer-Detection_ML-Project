# -*- coding: utf-8 -*-
"""10. Decision Tree Classification-Breast_Cancer_detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y_TtV8lwVpBfo76EhWDHJIoee_h0ye11

# Decision Tree Classification

## Business Problem-Breast Cancer Detection Problem

#### Import Library
"""

import pandas as pd
import numpy as np

"""### Load DataSet"""

from sklearn.datasets import load_breast_cancer
data =load_breast_cancer()

# Show The Data Data in form of Dictonary
data.data

# Feature Of Data
data.feature_names

# Target Data
data.target

# target Names
data.target_names

"""NOTES:--

    'malignant'=>Breast CANCER , target=0

    'benign'   =>Not Breast cancer ,target=1

##### Create Dataset In DataFrame aformat
"""

df=pd.DataFrame(np.c_[data.data,data.target],columns=[list(data.feature_names)+['target']])
df

df.tail()

# Shape OF data
df.shape

# Total Patient=569
# Patient features=31

"""## Split Data"""

"""
 1.iloc(axis=None) -> _iLocIndexer
Purely integer-location based indexing for selection by position.
2.} .iloc[] is primarily integer position based (from 0 to
length-1 of the axis), but may also be used with a boolean
array.

Allowed inputs are:
An integer, e.g. 5.
A list or array of integers, e.g. [4, 3, 0].
A slice object with ints, e.g. 1:7.
A boolean array.
"""


df.iloc[0]

df.iloc[[0]]

df.iloc[:,0:-1]

df.iloc[:,-1]

X=df.iloc[:,0:-1]    # All Data Except target
y=df.iloc[:,-1]      # target Data

# Train_Test_split
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

print("Shape Of X_train=",X_train.shape)
print("Shape Of X_test=",X_test.shape)
print("Shape Of y_train=",y_train.shape)
print("Shape Of y_test=",y_test.shape)

"""##### Till Here we Done Preprocessing

# Train Decision Tree C Classification Model
"""

from sklearn.tree import DecisionTreeClassifier

#DecisionTreeClassifier()
# PARAMETER =(*, criterion="gini", splitter="best", max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0, 
#              max_features=None, random_state=None, max_leaf_nodes=None, min_impurity_decrease=0, class_weight=None, ccp_alpha=0) -> None

classifier=DecisionTreeClassifier(criterion="gini")
# Train the model
classifier.fit(X_train,y_train)
#parameter  (X, y, sample_weight=None, check_input=True, X_idx_sorted="deprecated") -> DecisionTreeClassifier

# Check Accuracy
classifier.score(X_test,y_test)

"""#### Split data on entropy"""

classifier_entropy=DecisionTreeClassifier(criterion="entropy")
# Train the model
classifier_entropy.fit(X_train,y_train,)

# Check Accuracy
classifier_entropy.score(X_test,y_test)

"""##### Accuracy gets improved

#### Feature Scaling
"""

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
sc.fit(X_train,)   

 #Parameters
# X : {array-like, sparse matrix} of shape (n_samples, n_features)
#   The data used to compute the mean and standard deviation
# used for later scaling along the features axis.

#y : None

# Feature Scaling

X_train_sc=sc.transform(X_train)
X_test_sc=sc.transform(X_test)

classifier_sc=DecisionTreeClassifier(criterion="gini")
# Train the model
classifier_sc.fit(X_train_sc,y_train)
#Accuracy
classifier_sc.score(X_test_sc,y_test)

"""Accuracy Have Not much effect on Decision Tree So Either we Can use or Not 
Feature Scaling in Decision tree

### Pridict cancer
"""

patient1 = [17.99,
 10.38,
 122.8,
 1001.0,
 0.1184,
 0.2776,
 0.3001,
 0.1471,
 0.2419,
 0.07871,
 1.095,
 0.9053,
 8.589,
 153.4,
 0.006399,
 0.04904,
 0.05373,
 0.01587,
 0.03003,
 0.006193,
 25.38,
 17.33,
 184.6,
 2019.0,
 0.1622,
 0.6656,
 0.7119,
 0.2654,
 0.4601,
 0.1189]

# Converted into 2D
patient1 = np.array([patient1])
patient1

classifier.predict(patient1)

data.target_names

pred=classifier.predict(patient1)
pred

if pred[0]==0:
  print("Cancer Detected with malignant Tumer")
else:
  print("Cancer Not Detected with mbenign Tumer")

"""### Decision Tree Classification Notes:-

What is Decision Tree?
  
    Decision tree is a versatile machine Learnig Algorithms that can perform both classification and Regression tasks,and even multioutput task.

    Scikit-Learn uses the classification and Regression Tree (CART) algorithm to train the decision tree 

    Which produces only binary tree:nonleaf nodes always  have Two Children
    (ie-Q/s Only Answer in yes/No answers)


    Decision Tree
    1.Decision Tree Classification
    2.Decision Tree REgression

#### Mathematical Formula Of Decision Trees
    1.Gini Impurity
    2.Entropy
    3.CART Cost Function For Classification
    #### https://www.geeksforgeeks.org/gini-impurity-and-entropy-in-decision-tree-ml/
---

What IS Decision Tree Classification?

    In Decision Tree classification We Split the Node For That we Use Gini Impurity or Entropy

    In Decision Tree Regresion We Split the Data For That we Use MSE(Mean Square Error)


    ### https://www.javatpoint.com/machine-learning-decision-tree-classification-algorithm
"""

