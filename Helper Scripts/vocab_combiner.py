# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 20:57:46 2020

@author: Hardik
"""

##Vocab combiner##


def combine_vocab_src():
    f1=open("src-train-vocab.txt","rt",encoding="utf8")
    f2=open("src-test-vocab.txt","rt",encoding="utf8")
    f3=open("src-dev-vocab.txt","rt",encoding="utf8")
    f4=open('stc_combined_vocab',"w+",encoding="utf8")
    
    unique_tokens=set()
    row_count=0
    while True :
        text=f1.readline()
        if not text:
            break
        unique_tokens.add(text)
        row_count=row_count+1
    
    while True :
        text=f2.readline()
        if not text:
            break
        unique_tokens.add(text)
        row_count=row_count+1
    
    while True :
        text=f3.readline()
        if not text:
            break
        unique_tokens.add(text)
        row_count=row_count+1
    
    print(row_count)
    
    unique_tokens_list=list(unique_tokens)
    for i in range(len(unique_tokens_list)):
        f4.write(unique_tokens_list[i])
    
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    
combine_vocab_src()



#%%

def combine_vocab_tgt():
    f1=open("tgt-train-vocab.txt","rt",encoding="utf8")
    f2=open("tgt-test-vocab.txt","rt",encoding="utf8")
    f3=open("tgt-dev-vocab.txt","rt",encoding="utf8")
    f4=open('tgt_combined_vocab',"w+",encoding="utf8")
    
    unique_tokens=set()
    row_count=0
    while True :
        text=f1.readline()
        if not text:
            break
        unique_tokens.add(text)
        row_count=row_count+1
    
    while True :
        text=f2.readline()
        if not text:
            break
        unique_tokens.add(text)
        row_count=row_count+1
    
    while True :
        text=f3.readline()
        if not text:
            break
        unique_tokens.add(text)
        row_count=row_count+1
    
    print(row_count)
    
    unique_tokens_list=list(unique_tokens)
    for i in range(len(unique_tokens_list)):
        f4.write(unique_tokens_list[i])
    
    f1.close()
    f2.close()
    f3.close()
    f4.close()


combine_vocab_tgt()
