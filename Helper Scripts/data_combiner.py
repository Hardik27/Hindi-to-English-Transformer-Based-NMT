# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 23:36:24 2020

@author: Hardik
"""

def combine_data_src():
    f1=open("cleaned_train_en","rt",encoding="utf8")
    f2=open("cleaned_dev_en","rt",encoding="utf8")
    f3=open("cleaned_test_en","rt",encoding="utf8")
    f4=open('src_combined',"w+",encoding="utf8")
    
    data=list()
    row_count=0
    while True :
        text=f1.readline()
        if not text:
            break
        data.append(text)
        row_count=row_count+1
    
    while True :
        text=f2.readline()
        if not text:
            break
        data.append(text)
        row_count=row_count+1
    
    while True :
        text=f3.readline()
        if not text:
            break
        data.append(text)
        row_count=row_count+1
    
    print(row_count)
    
    for i in range(len(data)):
        f4.write(data[i])
    
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    
combine_data_src()

##src-1270463

#tgt-1270463

#%%



def combine_data_tgt():
    f1=open("cleaned_train_hi","rt",encoding="utf8")
    f2=open("cleaned_dev_hi","rt",encoding="utf8")
    f3=open("cleaned_test_hi","rt",encoding="utf8")
    f4=open('tgt_combined',"w+",encoding="utf8")
    
    data=list()
    row_count=0
    while True :
        text=f1.readline()
        if not text:
            break
        data.append(text)
        row_count=row_count+1
    
    while True :
        text=f2.readline()
        if not text:
            break
        data.append(text)
        row_count=row_count+1
    
    while True :
        text=f3.readline()
        if not text:
            break
        data.append(text)
        row_count=row_count+1
    
    print(row_count)
    
    for i in range(len(data)):
        f4.write(data[i])
    
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    
combine_data_tgt()