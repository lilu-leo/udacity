#!/usr/bin/python
#coding:utf-8
import sys

sys.path.append("../tools/")
from email_preprocess import preprocess

features_train, features_test, labels_train, labels_test = preprocess()

from sklearn.neighbors import NearestNeighbors

from sklearn import neighbors 
knn = neighbors.KNeighborsClassifier(weights='distance')  
#训练数据集  
knn.fit(features_train, labels_train)

score = knn.score(features_test, labels_test)

print score  


