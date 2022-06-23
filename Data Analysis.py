# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 18:53:54 2020

@author: Radwa
"""

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(r'gene_table.txt')
'''no.1'''
count2=len(data.gene_name)
print("the total of genes in data =",count2)
print('----------------///////////////////////////////////////////////////////////----------------')

print(data.groupby('gene_biotype').size())
print('----------------///////////////////////////////////////////////////////////----------------')

'''no.2'''
print ("the average",data.mean())
print ("the max",data.max())
print ("the min",data.min())
print ("the median",data.median())
print('----------------///////////////////////////////////////////////////////////----------------')

'''no.3'''
data.groupby('chromosome').hist()
plt.show()
sorted_data = data.chromosome.sort_index(axis = 0 , ascending = 'true');
print(sorted_data)
print('----------------///////////////////////////////////////////////////////////----------------')


'''no.4'''      
count=0
for x in data.strand:
    if(x=='+'):
        count+=1
print("the percentage of the + strand=",(count/count2)*100,"%")
print('----------------///////////////////////////////////////////////////////////----------------')

'''no.5'''
print("the ",data.groupby('gene_biotype').mean())

