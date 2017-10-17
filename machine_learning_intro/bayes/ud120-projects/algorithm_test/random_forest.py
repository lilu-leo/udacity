#!/usr/bin/python
#coding:utf-8
import sys

sys.path.append("../tools/")
from email_preprocess import preprocess

features_train, features_test, labels_train, labels_test = preprocess()

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)

#训练数据集  
clf.fit(features_train, labels_train)

score = clf.score(features_test, labels_test)

print score  


