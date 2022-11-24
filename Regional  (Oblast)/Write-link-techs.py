# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 10:22:52 2022

@author: Harrie
"""


import ruamel.yaml as yaml
import pandas as pd
import numpy
import json

# with open("link-all-neighbours.yaml") as file:
#     try:
#         databaseConfig = yaml.safe_load(file)
#         print(databaseConfig)
#     except yaml.YAMLError as exc:
#         print(exc)
        
# ##        
        
        
excel= pd.read_excel(r'C:\Users\Harrie\Desktop\Thesis\data\Transmission\Transmission.xlsx')
df= pd.DataFrame(excel, columns=['FT',"Capacity"])


def build_links(n):
    d_energy_cap = {"energy_cap": int(df.at[n,'Capacity'])}
    d_constraints= {"constraints": {"energy_cap": d_energy_cap}}
    d_ac_transmission = {"ac_transmission": d_constraints}
    d_techs = {"techs": d_ac_transmission}
    d_region = {df.at[n,'FT']: d_techs}
    #d_links = {"Links": d_region}
    d_links['Links'][df.at[n,'FT']] = d_region
    return d_links





d_links['Links'][df.at[2,'FT']]= d_region
for n in range(len(df)):
    d_links = build_links(n)

with open('UA-Link-all-neigbours.yaml', "w") as f:
      yaml.dump(d_links, f)
     
     
