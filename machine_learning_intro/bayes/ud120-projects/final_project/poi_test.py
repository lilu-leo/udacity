
file = open("poi_names.txt")

list = []

for line in file:
	line = line.replace(',', '').replace('(y)', '').replace('(n)','')
#	print line
	list.append(line.lstrip())
#print list

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#print enron_data

#print 'James Prentice'.upper() in enron_data.keys()

#print enron_data["PRENTICE JAMES"]["total_stock_value"]

#print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

#print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

salary_count = 0
email_count = 0
salary_nan_count = 0
total_count = 0
for key in enron_data:
	total_count += 1
	if (enron_data[key]['salary'] != 'NaN'):
		salary_count += 1
	if (enron_data[key]['email_address'] != 'NaN'):
                email_count += 1
	if (enron_data[key]['total_payments'] == 'NaN'):
                salary_nan_count += 1

print float(salary_nan_count*1.0/total_count)
print 'salary_nan_count ', salary_nan_count
print 'total_count', total_count

print 'email_count' + str(email_count)
print 'salary_count' + str(salary_count)

poi_count = 0
poi_nan_count = 0
for key in enron_data:
#	print enron_data[key]['poi']
	if (enron_data[key]['poi'] == True):
		poi_count += 1
	#	print 'poi_count' , poi_count
		if (enron_data[key]['total_payments'] == 'NaN'):
			poi_nan_count += 1
			print 'poi_nan_count is : ', poi_nan_count
print 'poi count' , poi_count
print "poi_nan_count percent " + str(poi_nan_count * 1.0/poi_count) 


print '----------'
poi_list = []
for key in enron_data:
        if (enron_data[key]["poi"]==1):
                poi_list.append(key)
#		print key

print len(list)

import re
count = 0

line = 0

for item in list:
	for poi_item in poi_list:
		m = poi_item.lower().find(item.lower())
		line += 1
#		print poi_item.lower()
#		print item.lower()
#		print m 
		if(m >= 0):
			count += 1

print count






