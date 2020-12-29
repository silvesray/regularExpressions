# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 17:33:36 2020

@author: Melan
"""
import re
import os
import pandas as pd
files = None

os.chdir("F:/OpenClassRoom/regularExpression")
with open("data.txt", 'r') as file:
    files= file.readlines()

sample = files[:5]
pattern_name = r"[A-Za-z]+\s[A-Za-z]+\n$"
pattern_contact = r"^[0-9]{3}([ .-]?[0-9]{2,}){2}"
pattern_mail = r"[A-Za-z0-9]+@[A-Za-z]+"

pattern_compile = re.compile(pattern_name)
pattern_contact = re.compile(pattern_contact)
pattern_mail = re.compile(pattern_mail)

names = [d for d  in files if pattern_compile.search(d)!= None]
contacts = [d for d in files if pattern_contact.search(d)!= None]
mails = [d for d in files if pattern_mail.search(d)!= None]

df_dict = {'Names': names, 'Contacts': contacts, 'Mails': mails}
df = pd.DataFrame.from_dict(df_dict, orient="index")
df = df.transpose()
print(df.head())