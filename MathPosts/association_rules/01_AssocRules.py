# -*- coding: utf-8 -*-
"""
Example of using association rules
to conduct conjunctive analysis

First script builds the dataset

@author: Andy Wheeler
"""

import os
import itertools
import pandas as pd
import numpy as np
import scipy.sparse
import mlxtend.frequent_patterns as fp

os.chdir(r'C:\Users\andre\OneDrive\Desktop\association_rules')
crim_dat = pd.read_csv('NIBRS_DummyDat.csv')

def pd_sparse(df):
    mb = df.memory_usage().sum()/1e6
    print(f'Original Memory: {mb} (mega bytes)')
    sp = scipy.sparse.csr_matrix(df.values)
    update = pd.DataFrame.sparse.from_spmatrix(sp, columns=list(df))
    mb2 = update.memory_usage().sum()/1e6
    print(f'Sparse Memory: {mb2} (mega bytes)')    
    return update

crim_dat = pd_sparse(crim_dat)

#################################################################
#ASSOCIATION RULE ANALYSIS

#Function to check if in list
def nope_check(x, np_li):
    for i in np_li:
        if i <= x:
            return True
    return False

def freq_sets(data,limit,max_len):
    #Round 1, getting columns that have at least above limit
    tot_fo = data.sum(axis=0)
    sub_fo = tot_fo[tot_fo > limit]
    singles = [set([i]) for i in sub_fo.index]
    fin_list = singles.copy()
    fin_val = list(sub_fo)
    nope = []
    print(f'Finished Round 1, total {len(singles)} singlets')
    #Round 2, all pairwise with those who passed R1
    add_check = []
    for left, right in itertools.combinations(singles,2):
        li= list(left) + list(right)
        sli = set(li)
        tot_n = data[li].product(axis=1).sum()
        if tot_n > limit:
            fin_list.append(sli)
            fin_val.append(tot_n)
            add_check.append(sli)
        else:
            nope.append(sli)        
    print(f'Finished Round 2, total {len(add_check)} doubles')
    #Round 3 to max len now
    single_str = [list(i)[0] for i in singles]
    for i in range(max_len-2):
        if len(add_check) == 0:
            break
        else:
            add_checknew = []
            for left,right in itertools.product(single_str, add_check):
                li = [left] + list(right)
                sli = set(li)
                if left in right:
                    pass
                elif sli in fin_list:
                    pass
                elif nope_check(sli, nope):
                    pass
                else:
                    tot_n = data[li].product(axis=1).sum()
                    if tot_n > limit:
                        fin_list.append(sli)
                        fin_val.append(tot_n)
                        add_checknew.append(sli)
                    else:
                        nope.append(sli)
        del add_check
        print(f'Finished round {i+3}, total new sets {len(add_checknew)}')
        add_check = add_checknew.copy()
    #Now formatting as a table to return
    freq_set = pd.DataFrame(zip(fin_list, fin_val), columns=['itemsets','freq'])
    freq_set['support'] = freq_set['freq']/data.shape[0]
    freq_set['itemsets'] = freq_set['itemsets'].apply(frozenset)
    var_order = ['support','itemsets','freq']
    return freq_set[var_order]

res = freq_sets(crim_dat,limit=1000,max_len=7)
#################################################################



#################################################################
#ASSOCIATION RULE ANALYSIS

#Itemsets that occur at least in 5% of the cases
#freq_items = fp.apriori(crim_dat, min_support=0.01, max_len=6, use_colnames=True) 
#will get memory errors if you try to scrape out itemsets with lower support

#check if LEO_Assault is within the frequent itemset
def check_set(x,low):
    return set(low) <= x

leo = ['ass_LEO_Assault']

print(f'Total number of LEO assaults in Data {crim_dat[leo].sum()}')
check_res = res['itemsets'].apply(lambda x: check_set(x, low=leo))
res[check_res]

res.to_csv('freq_sets.csv', index=False)

#Select out those with an assault type as one of the vars, then do 
#Association rules on that limited set, then only look at consequents
#rules = fp.association_rules(freq_items, metric="confidence", min_threshold=0.7)
rules = fp.association_rules(res, metric="confidence", min_threshold=0.7)

check_off_assault = rules['consequents'] == frozenset(['rel_Known'])
vars = ['antecedents','consequents', 'confidence', 'lift']
print( rules.loc[check_off_assault, vars] )

rules.to_csv('rules.csv',index=False)

#################################################################


#################################################################
#Maybe also show RuleFit example?
#https://github.com/christophM/rulefit
#################################################################