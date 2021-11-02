#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import os

'''
input parameters
'''

dest_folder = 'women-tops'
input_xlsx = 'scraping-attributes-list-women-tops.xlsx'

'''
read input xlsx file
'''
df_to_scrap = pd.read_excel(input_xlsx)
cols = list(df_to_scrap.columns)

'''
create destination folder
'''
if not os.path.exists(dest_folder):
    os.mkdir(dest_folder)
    print(f'{dest_folder} created successfully')

'''
Read txt from multidir.sh
'''

data=[]
with open('multidir.sh','r') as f:
    for txt in f.readlines():
        data.append(txt)

current_path = os.path.realpath('./')
for col in cols:
    if not os.path.exists(f'{dest_folder}/{col}'):
        os.makedirs(f'{dest_folder}/{col}')
    '''
    with open(f'{folder_name}/{col}/multidir.sh','w') as w:
        for i,txt in enumerate(data):
            if i ==0:
                w.write(txt)
                for val in df_to_scrap[col].dropna():
                    w.write(val+'\n')
            else:
                w.write(txt)
    '''
    os.chdir(f'{current_path}/{dest_folder}/{col}/')
    print(os.path.realpath('./'))
    os.system('multidir.sh')
    os.chdir(current_path)




