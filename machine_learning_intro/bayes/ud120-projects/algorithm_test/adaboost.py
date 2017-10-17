#!/usr/bin/python
#coding:utf-8
import sys

sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn.ensemble import AdaBoostClassifier
#训练数据集  

clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=2, min_samples_split=20, min_samples_leaf=5),
                         algorithm='SAMME',
                         n_estimators=300, learning_rate=0.8)
clf.fit(features_train, labels_train)
score = clf.score(features_test, labels_test)

print score  


