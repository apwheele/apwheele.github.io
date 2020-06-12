# -*- coding: utf-8 -*-
"""
Example of using association rules
to conduct conjunctive analysis

First script builds the dataset

@author: Andy Wheeler
"""

import os
import pandas as pd
import numpy as np
#import mlxtend.frequent_patterns as fp

os.chdir(r'C:\Users\andre\OneDrive\Desktop\association_rules')

#################################################################
#DATA PREP

#make a function to return cum-sum encoding for multiple columns
#of the same attribute
def encode_mult(df, cols, encode=None, base="V", cum=False):
	res_counts = []
	if not encode:
		tot_encode = pd.unique(df[cols].values.ravel())
	else:
	 	tot_encode = encode
	var_names = []
	for i,v in enumerate(tot_encode):
		var_name = base + str(i)
		res_count = (df[cols] == v).sum(axis=1)
		res_counts.append( res_count )
		var_names.append(var_name)
	res_count_df = pd.concat(res_counts, axis=1)
	res_count_df.columns = var_names
	if cum:
		return res_count_df, list(tot_encode)
	else:
		return 1*(res_count_df > 0), list(tot_encode)

#Only read in particular columns that I want
    
assault_type = ['V4023' + str(i+1) for i in range(3)]
relationship = ['V4032' + str(i+1) for i in range(3)]
ucr_off = ['V2006' + str(i+1) for i in range(3)]
drug_inv = ['V2009' + str(i+1) for i in range(3)]
weapon = ['V2017' + str(i+1) for i in range(3)]

keep_cols = assault_type + relationship + ucr_off + drug_inv + weapon
nibrs = pd.read_csv('NIBRS_2012.csv', usecols=keep_cols)

print( nibrs.shape )
print( nibrs.memory_usage() )

#To check out the full file
#test_file = pd.read_csv('NIBRS_2012.csv', nrows=5)

#Work with a smaller file to get your code working
#nibrs = nibrs.sample(10000)

#Recoding several columns, making a function to do this for NIBRS
#Specifically

def print_count(dat, cols):
    np_cnt = np.unique( dat[cols].values.ravel(), return_counts=True)
    res_df = pd.DataFrame( np_cnt, index=['Labels','Counts']).T
    print(res_df)

def recode_nibrs(codes, columns, data):
    rep_dict = {}
    for b,e,l in codes:
        curr_dict = {i:l for i in range(b,e+1)}
        rep_dict.update(curr_dict)
    var_dict = {i:rep_dict for i in columns}
    data.replace(var_dict, inplace=True)
    print_count(dat=data, cols=columns)

rel_code = [(-100,0,'Missing'), 
            (1,13,'Family'),
            (14,24,'Known'),
            (25,25,'Outside'),
            (25,100,'Missing')]

recode_nibrs(rel_code, relationship, nibrs)

ass_code = [(-100,0,'Missing'),
            (1,1,'Argument'),
            (2,2,'LEO_Assault'),
            (3,5,'DrugGangAssault'),
            (6,6,'LoversQuarrelAssault'),
            (7,9,'OtherFelony'),
            (10,19,'Missing'),
            (20,20,'JustHomicide'),
            (21,29,'Missing'),
            (30,34,'NegManslaughter'),
            (35,100,'Missing')]
            
recode_nibrs(ass_code, assault_type, nibrs)

ucr_code = [(-100,90,'Missing'),
            (91,93,'Homicide'),
            (94,99,'Missing'),
            (100,114,'Kidnap_SexOff'),
            (115,199,'Missing'),
            (120,120,'Robbery'),
            (121,130,'Missing'),
            (131,133,'Assault'),
            (134,199,'Missing'),
            (200,200,'Arson'),
            (201,209,'Missing'),
            (210,210,'Fraud_StolenProp'),
            (220,220,'Burglary'),
            (231,238,'Larceny'),
            (240,240,'MVTheft'),
            (250,280,'Fraud_StolenProp'),
            (290,290,'Vandalism'),
            (351,352,'Drug'),
            (361,370,'Kidnap_SexOff'),
            (391,394,'Gambling'),
            (401,403,'Prostitution'),
            (510,510,'Bribery'),
            (520,520,'WeaponViol'),
            (641,642,'Kidnap_SexOff'),
            (642,1000,'Missing')]

recode_nibrs(ucr_code, ucr_off, nibrs)

drug_code = [(-10,0,'Missing'),
             (1,1,'AlcoholUse'),
             (2,2,'DrugUse'),
             (3,3,'ComputerUse')]

recode_nibrs(drug_code, drug_inv, nibrs)

weap_code = [(-100,0,'Missing'),
             (110,151,'Firearm'),
             (200,200,'Knife'),
             (300,300,'BluntObject'),
             (350,350,'MVWeap'),
             (400,400,'Fists'),
             (500,900,'OtherWeap'),
             (990,990,'NoWeap')]

recode_nibrs(weap_code, weapon, nibrs)

#Now making the one-hot encoded columns
assOH,assVars = encode_mult(nibrs, assault_type, base="ass_")
relOH,relVars = encode_mult(nibrs, relationship, base="rel_")
ucrOH,ucrVars = encode_mult(nibrs, ucr_off, base="ucr_")
druOH,druVars = encode_mult(nibrs, drug_inv, base="drug_")
weaOH,weaVars = encode_mult(nibrs, weapon, base="weap_")
OH_data = pd.concat([assOH,relOH,ucrOH,druOH,weaOH],axis=1)
var_list = assVars + relVars + ucrVars +druVars + weaVars

#Getting rid of the missing data columns
var_OH = list(OH_data)
miss_cols = [var_OH[i] for i in range(len(var_list)) if var_list[i] == 'Missing']
fin_cats = [i for i in var_list if i != 'Missing']
OH_data.drop(miss_cols, axis=1, inplace=True)

#Check out all the variables now
print( list(OH_data) )

print( OH_data.shape )
print( OH_data.memory_usage() )

#replace names after _
sub_names = []
for nam,var in zip( list(OH_data), fin_cats):
    sub = nam.split("_")[0] + "_" + var
    sub_names.append(sub)
    
OH_data.columns = sub_names

#Save to a pickle for later use?
OH_data.to_csv('NIBRS_DummyDat.csv',index=False)
#################################################################
