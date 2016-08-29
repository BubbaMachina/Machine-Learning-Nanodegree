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

import pandas as pd

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

print "\n creating a data frame of enron data \n"

print "\n enron data \n"

print enron_data

print "\n keys of enron data \n"

print keys

enron_df_columns_list = list()

enron_df_columns_list.append('name')

for col in enron_data[keys[0]].keys():
    enron_df_columns_list.append(col)

print "\n columns created for enron data df \n"

enron_df_columns = ','.join(enron_df_columns_list)

print enron_df_columns


"""
#enron_data[keys[0]]["name"] = keys[0]

#enron_data_df = pd.DataFrame(columns= enron_df_columns_list)

#enron_data_df["name"] = keys

#print enron_data_df.head()

#print "\n empty enron data df \n"

#print enron_data_df

#print "\n appending the enron data into the df \n"

#print enron_data.keys()[0]

#print enron_data[keys[0]]

#enron_data[keys[0]]['name'] = keys[0]

"""

print '\n Creating enron data list\n '

print (enron_data[keys[0]])

enron_data_list = list()
#sub_key_list = list()

for key in keys:
    #print key

    sub_key_list = list()

    enron_data[key]["name"] = key

    for sub_key in enron_df_columns_list:
        #print sub_key

        #print enron_data[key][sub_key]

        sub_key_list.append(enron_data[key][sub_key])

    enron_data_list.append(sub_key_list)

        #print sub_key_list
print enron_data_list

"""

#enron_data[keys[1]]["name"] = keys[1]

#print pd.Series(enron_data[keys[0]])

#enron_data_df.loc[0] = pd.Series(enron_data[keys[0]])

#enron_data_df.append(pd.Series(enron_data[keys[1]]),ignore_index= True)

#print "\n appending the df\n"

#print enron_data_df.head()
'''
for name in enron_data:
    #print name
    #print enron_data[name]

    enron_data[name]['name'] = name

    #print enron_data[name].keys()

    #print enron_data[name].values()



    df = pd.DataFrame([enron_data[name]])

    enron_data_df.append(df)

    #print df
    #enron_data_df.append(df)

    #enron_data_df



    #rint df


    #print df

    #print df.shape[0]

    #enron_data_df.loc[enron_data_df["name"] == name] = df.values

    #enron_data_df.append(df)

    #print enron_data_df

print "done \n"

print enron_data_df.head()

#print enron_data_df

print df.head()

#enron_data_df = pd.DataFrame(enron_data[])

#print enron_data_df.head()

'''
"""


print "\n creating a df \n"

enron_data_df = pd.DataFrame(enron_data_list, columns=enron_df_columns_list)

print enron_data_df.head()

print enron_data_df.shape

print "how many folks have quantified salary? and know many have emails?"

print "\n quantified salary\n"

print enron_data_df['email_address'][enron_data_df["salary"] != 'NaN'].shape[0]

print "\n and have know emails \n"

print enron_data_df['email_address'][enron_data_df["email_address"] != 'NaN'].shape[0]

print ("\n How many people in the E+F dataset (as it currently exists) ")

print  ("have NaN for their total payments? What percentage of people in the dataset as a whole is this? \n")

print "\nhave NaN for their total payments? \n "

print enron_data_df["total_payments"][enron_data_df["total_payments"] == 'NaN'].shape[0]

perct_total_payment = (
    float(enron_data_df["total_payments"][enron_data_df["total_payments"] == 'NaN'].shape[0])

    /

    float(enron_data_df.shape[0]))

print (perct_total_payment * 100 )

print enron_data_df.shape[0]

print "\n How many POIs in the E+F dataset have NaN for their total payments?"

print "What percentage of POI\'s as a whole is this? \n "

print enron_data_df["total_payments"][enron_data_df["poi"] == True].shape[0]


percentage_poi= (
    float((enron_data_df["total_payments"][enron_data_df["total_payments"] == 'NaN']
          [enron_data_df["poi"] == True]).shape[0])

    /

    float(enron_data_df.shape[0]))

print percentage_poi


