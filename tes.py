# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:31:16 2021

@author: WINDOWS 10
"""

import json
import pyarrow.lib as _lib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

f = open ("C:\\Users\\WINDOWS 10\\Kuliah\\kode_negara_lengkap.json")
file_json = json.load(f)
df_csv = pd.read_csv("C:\\Users\\WINDOWS 10\\Kuliah\\produksi_minyak_mentah.csv")
df_json = pd.DataFrame.from_dict(file_json,orient='columns')
st.set_option('deprecation.showPyplotGlobalUse', False)

#1
N = st.text_input("Masukkan nama negara: ")
 
list1 = []

for i in list(df_csv['kode_negara']):
    if i not in list(df_json['alpha-3']):
        list1.append(i)

for i in list1:
    df_csv = df_csv[df_csv.kode_negara !=i]

nama_negara = []
"""for i in range(len(df_csv)):
    for j in range(len(df_json)):
        if list(df_csv['kode_negara'])[i] == list(df_json['alpha-3'])[j]:
            nama_negara.append(list(df_json['name'])[j])
            
df_csv['negara'] = nama_negara"""

df1 = df_csv.loc[df_csv['kode_negara']==N]

graphA = plt.subplot()
df1.plot(x='tahun', y='produksi')
graphA = plt.show()
st.pyplot(graphA)

#2
tahun = []
for i in list(df_csv['tahun']):
    if i not in tahun:
        tahun.append(i)
Y = st.selectbox("Masukkan tahun: ",tahun)
Y = int(Y)
C1 = st.number_input("Masukkan banyak negara: ",min_value=1)
C1 = int(C1)

df2 = df_csv.loc[df_csv['tahun'] == Y]
df2 = df2.sort_values(by=['produksi'], ascending=False)
df3 = df2[:C1]

df3.plot.bar(x='kode_negara', y='produksi')
graphB = plt.show()
st.pyplot(graphB)

#3
list2 = []
kumulatif = []

C2 = st.number_input("Masukkan banyak negara: ", min_value=1, key = "C2")
C2 = int(C2)
for i in list(df_csv['kode_negara']):
    if i not in list2:
        list2.append(i)

for i in list2:
    a = df_csv.loc[df_csv['kode_negara'] == i, 'produksi'].sum()
    kumulatif.append(a)
    
df_kumulatif = pd.DataFrame(list(zip(list2, kumulatif)), columns = ['kode_negara', 'kumulatif'])
df_kumulatif = df_kumulatif.sort_values(by=['kumulatif'], ascending = False)
df_kumulatif2 = df_kumulatif[:C2]

df_kumulatif2.plot.bar(x= 'kode_negara', y= 'kumulatif')
graphC = plt.show()
st.pyplot(graphC)

#4
# Part 1
jumlah_produksi = df2[:1].iloc[0]['produksi']
kode_negara = df2[:1].iloc[0]['kode_negara']
nama_negara = ""
region_negara = ""
subregion_negara = ""

for i in range (len(df_json)):
    if list(df_json['alpha-3'])[i] == kode_negara:
        nama_negara = list(df_json['name'])[i]
        region_negara = list (df_json['region'])[i]
        subregion_negara = list(df_json['sub-region'])[i]

print("Negara yang memiliki jumlah produksi minyak terbesar pada tahun {}".format(Y))
print("{} \n{} \n{} \n{} \n{}".format(jumlah_produksi, kode_negara, nama_negara, region_negara, subregion_negara))

jumlah_produksi = df_kumulatif[:1].iloc[0]['kumulatif']
kode_negara = df_kumulatif [:1].iloc[0]['kode_negara']
nama_negara = ""
region_negara = ""
subregion_negara = ""

for i in range(len(df_json)):
    if list (df_json['alpha-3'])[i] == kode_negara:
        nama_negara = list(df_json['name'])[i]
        region_negara = list(df_json['region'])[i]
        subregion_negara = list(df_json['sub-region'])[i]

st.markdown(" ## Negara yang memiliki jumlah produksi minyak terbesar pada keseluruhan tahun")
st.text ("{} \n{} \n{} \n{} \n{}".format(jumlah_produksi, kode_negara, nama_negara, region_negara, subregion_negara))

# Part 2
df_terkecil = df2[df2.produksi !=0]
df_terkecil = df_terkecil.sort_values(by=['produksi'], ascending=True)

jumlah_produksi = df_terkecil [:1].iloc[0]['produksi']
kode_negara = df_terkecil[:1].iloc[0]['kode_negara']
nama_negara = ""
region_negara = ""
subregion_negara = ""

for i in range(len(df_json)):
    if list(df_json['alpha-3'])[i] == kode_negara:
        nama_negara = list (df_json['name'])[i]
        region_negara = list(df_json['region'])[i]
        subregion_negara = list(df_json['sub-region'])[i]

st.markdown("Negara yang memiliki jumlah produksi minyak terkecil pada tahun {}".format(Y))
st.text("{} \n{} \n{} \n{} \n{}".format(jumlah_produksi, kode_negara, nama_negara, region_negara, subregion_negara))

dfkumulatifterkecil = df_kumulatif[df_kumulatif.kumulatif != 0]
dfkumulatifterkecil = dfkumulatifterkecil.sort_values(by=['kumulatif'], ascending=True)

jumlah_produksi = dfkumulatifterkecil [:1].iloc[0]['kumulatif']
kode_negara = dfkumulatifterkecil[:1].iloc[0]['kode_negara']
nama_negara = ""
region_negara = ""
subregion_negara = ""

for i in range(len(df_json)):
    if list(df_json['alpha-3'])[i] == kode_negara:
        nama_negara = list (df_json['name'])[i]
        region_negara = list(df_json['region'])[i]
        subregion_negara = list(df_json['sub-region'])[i]
        
print("Negara yang memiliki jumlah produksi minyak terkecil pada keseluruhan tahun")
print("{} \n{} \n{} \n{} \n{}".format(jumlah_produksi, kode_negara, nama_negara, region_negara, subregion_negara))

# Part 3
df_produksi_nol = df2[df2.produksi == 0]
listnegara_nol = []
listregion_nol = []
listsubregion_nol = []

for i in range (len(df_produksi_nol)):
    for j in range (len(df_json)):
        if list(df_produksi_nol['kode_negara'])[i] == list(df_json['alpha-3'])[j]:
            listnegara_nol.append(list(df_json['name'])[j])
            listregion_nol.append(list(df_json['region'])[j])
            listsubregion_nol.append(list(df_json['sub-region'])[j])

df_produksi_nol['negara']= listnegara_nol
df_produksi_nol['region']= listregion_nol
df_produksi_nol['sub-region']= listsubregion_nol

dfkumulatif_nol = df_kumulatif[df_kumulatif.kumulatif == 0]
listnegara_kumulatifnol = []
listregion_kumulatifnol = []
listsubregion_kumulatifnol = []

for i in range(len(dfkumulatif_nol)):
    for j in range (len(df_json)):
        if list (dfkumulatif_nol['kode_negara'])[i] == list(df_json['alpha-3'])[j]:
            listnegara_kumulatifnol.append(list(df_json['name'])[j])
            listregion_kumulatifnol.append(list(df_json['region'])[j])
            listsubregion_kumulatifnol.append(list(df_json['sub-region'])[j])

dfkumulatif_nol['negara'] = listnegara_kumulatifnol
dfkumulatif_nol['region'] = listregion_kumulatifnol
dfkumulatif_nol['sub-region'] = listsubregion_kumulatifnol

st.dataframe(df_produksi_nol)
st.table(dfkumulatif_nol)

