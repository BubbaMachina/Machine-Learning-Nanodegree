#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import numpy as np

import pickle

import re

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print enron_data.keys()

# how many people are in the list
print len(enron_data.keys())

#number of features for each person
for feature in (enron_data.values()):
    print feature.keys()
    print len(feature.keys())
    break

poi_count = 0

for person in enron_data.keys():
    if enron_data[person]["poi"] == 1:
        poi_count +=1

print "\n poi count"
print poi_count


name_file = open("../final_project/poi_names.txt","r").read()

"""
for line in name_file:
    if ")" in line:
        print line.split()[1], line.split()[2]
        """

#for line in name_file
names_poi = re.findall(" (.*)",name_file)

print names_poi

print len(names_poi)

print "\nWhat is the total value of the stock belonging to James Prentice?\n"

#print enron_data["Prentice James"].values()

keys = enron_data.keys()

#print keys

for key in keys:

    #print key

    find_james = re.findall("[J]\S.+", key)

    if len(find_james)> 0:
        print find_james

#print keys

print "\n James Prentice's total value of stock \n"
print enron_data['PRENTICE JAMES']['total_stock_value']

print "\n How many email messages do we have from Wesley Colwell to persons of interest? \n"

print enron_data["COLWELL WESLEY"]['from_this_person_to_poi']

print "\n Whats the value of stock options exercised by Jeffrey K Skilling \n"

for key in keys:

    #print key

    find_jeff_k = re.findall("[S]\S.+", key)

    if len(find_jeff_k)> 0:
        print find_jeff_k

print "\n \n"

print "\n Whats the value of stock options exercised by Jeffrey K Skilling \n"

print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print "\n Of these three individuals 'Lay, Skilling and Fastow' \n"

print "who took home the most money (largest value of 'total_payments' feature)? \n"

print "\n checking the keys of the POIs \n"

print enron_data['SKILLING JEFFREY K'].keys()

print "\n finding Lay, Skilling and Fastow \n"

find_three_poi_list = list()
for key in keys:

    #print key

    find_three_poi = re.findall("[FLS]\S.+", key)

    if len(find_three_poi)> 0:
        #print find_three_poi

        find_three_poi_list.append(find_three_poi[0])

print sorted(find_three_poi_list)

print "\n finding Lay, SKilling and Fastows total payments\n"

print "\n FASTOW ANDREW S total payments\n "

print enron_data['FASTOW ANDREW S']['total_payments']

print "\n LAY KENNETH L total payments \n "

print enron_data['LAY KENNETH L']['total_payments']

print "\n 'SKILLING JEFFREY K'total payments\n "

print enron_data['SKILLING JEFFREY K']['total_payments']

largest_total_payment = np.array([enron_data['FASTOW ANDREW S']['total_payments'],

                                 enron_data['LAY KENNETH L']['total_payments'],

                                 enron_data['SKILLING JEFFREY K']['total_payments']])

print "\n Who got the largest payment? \n"

print largest_total_payment.max()

print "LAY KENNETH L"

print type(enron_data['METTS MARK']['deferral_payments'])

print enron_data






