# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 17:33:36 2020

@author: Melan
"""
import re
import os
import pandas as pd


current_path = os.path.dirname(__file__)
os.chdir(current_path)

def extractInfo(filename):
    """
    get informations about someone according a text 

    Parameters
    ----------
    filename : string
        DESCRIPTION.

    Returns
    -------
    dataframe.

    """
    # check if the filename is a txt extension
    
    dictPattern= {
        "patName" : r"[A-Za-z]+\s[A-Za-z]+\n$",
        "patContact" : r"^[0-9]{3}([ .-]?[0-9]{2,}){2}",
        "patMail" : r"[A-Za-z0-9]+@[A-Za-z]+",
        "patAd" : r"^[0-9]{2,}\s\w+\s+\w+"}
    
    _, ext = os.path.splitext(filename)
    assert ext == ".txt", "The file was not a file text"
    with open(filename, "r") as f:
        content = f.readlines()
            
    name_compile = re.compile(dictPattern.get("patName"))
    contact_compile = re.compile(dictPattern.get("patContact"))
    mail_compile = re.compile(dictPattern.get("patMail"))
    adress_compile = re.compile(dictPattern.get("patAd"))
    
    names = [d.rstrip() for d  in content if name_compile.search(d)!= None]
    contacts = [d.rstrip() for d in content if contact_compile.search(d)!= None]
    mails = [d.rstrip() for d in content if mail_compile.search(d)!= None]
    adresses = [d.rstrip() for d in content if adress_compile.search(d) != None]
    
    
    
    df_dict = {'Names': names, 'Contacts': contacts, 'Mails': mails,'Adresses': adresses }
    df = pd.DataFrame.from_dict(df_dict, orient="index")
    df = df.transpose()
    return df
