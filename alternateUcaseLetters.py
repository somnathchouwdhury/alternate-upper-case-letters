#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 19:25:46 2021

@author: samac
"""

n=input()
res=""
j=0
for i in range(len(n)):
    if j%2==1:
        if n[i]>='A' and n[i]<='Z' :
            ch=chr(ord(n[i])+32)
            res=res+ch
        else:
            res=res+n[i]
    else:
        if n[i] >= 'a' and n[i] <= 'z':
            ch=chr(ord(n[i])-32)
            res=res+ch
        else:
            res=res+n[i]
    if n[i]==' ':
        continue
    j=j+1
    
print(res)