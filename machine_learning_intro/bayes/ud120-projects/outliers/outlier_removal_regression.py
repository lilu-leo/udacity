#!/usr/bin/python

import random
import numpy
import matplotlib.pyplot as plt
import pickle

from outlier_cleaner import outlierCleaner


### load up some practice data with outliers in it
ages = pickle.load( open("practice_outliers_ages.pkl", "r") )
net_worths = pickle.load( open("practice_outliers_net_worths.pkl", "r") )


### ages and net_worths need to be reshaped into 2D numpy arrays
### second argument of reshape command is a tuple of integers: (n_rows, n_columns)
### by convention, n_rows is the number of data points
### and n_columns is the number of features
ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))
from sklearn.cross_validation import train_test_split
ages_train, ages_test, net_worths_train, net_worths_test = train_test_split(ages, net_worths, test_size=0.1, random_state=42)

### fill in a regression here!  Name the regression object reg so that
### the plotting code below works, and you can see what your regression looks like


from sklearn import linear_model
reg = linear_model.LinearRegression()

print 'ages_train : ', ages_train
print 'net_worths_train : ', net_worths_train

reg.fit(ages_train, net_worths_train)
print reg.coef_

print reg.score(ages_test, net_worths_test)

try:
    plt.plot(ages, reg.predict(ages), color="blue")
except NameError:
    pass
plt.scatter(ages, net_worths)
#plt.show()

print reg.coef_
print reg.intercept_
print reg.score(ages_test, net_worths_test);

### identify and remove the most outlier-y points
cleaned_data = []
try:
    predictions = reg.predict(ages_train)
    print 'predictions lenth is : ', len(predictions)
    print 'ages_train :' , len(ages_train)
    cleaned_data = outlierCleaner( predictions, ages_train, net_worths_train )
    print 'clean data len is : ', len(cleaned_data)

    reg.fit(ages_train, net_worths_train)
    print 'clean data : ', cleaned_data
    print 'reg.coef_', reg.coef_
except NameError:
    print "your regression object doesn't exist, or isn't name reg"
    print "can't make predictions to use in identifying outliers"


### only run this code if cleaned_data is returning data
if len(cleaned_data) > 0:
    ages, net_worths, errors = zip(*cleaned_data)

    temp_age = []
 
    list_ages = list(ages)    

    for item in ages:
        temp = []
        temp.append(item)
        temp_age.append(temp)    

#temp_age.append(list_ages)

    temp_net_worths = []
    
    for item in net_worths:
	temp = []
	temp.append(item)
	temp_net_worths.append(temp)

    #temp_net_worths.append(list(net_worths))
    print temp_age

    print 'temp_age len :' , len(temp_age)
    print 'temp_net_worths : ' , len(temp_net_worths)

    print 'temp age : ', temp_age
    print 'tem_net_worths :' , temp_net_worths    


    reg.fit(temp_age, net_worths)
    print 'reg.coef_', reg.coef_
    
    print reg.score(ages_test, net_worths_test)
    ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
    net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))

    ### refit your cleaned data!
    try:
        reg.fit(ages, net_worths)
        plt.plot(ages, reg.predict(ages), color="blue")
    except NameError:
        print "you don't seem to have regression imported/created,"
        print "   or else your regression object isn't named reg"
        print "   either way, only draw the scatter plot of the cleaned data"
    plt.scatter(ages, net_worths)
    plt.xlabel("ages")
    plt.ylabel("net worths")
    plt.show()


else:
    print "outlierCleaner() is returning an empty list, no refitting to be done"

