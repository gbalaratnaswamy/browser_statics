import pandas as pd 
import numpy as np
from bs4 import BeautifulSoup
import requests
from cfg import *
from matplotlib import pyplot
from datetime import datetime
# function to create dataframe from data
def create_db_from_data(year,data,columns):
    month=data[0]
    data.insert(0,year)
    temp={key : [data[i]] for i,key in enumerate(columns)}
    return pd.DataFrame(temp)

# clean data and convert to int
def clean_data(data):
    res=[data[0]]
    for value in data[1:]:
        res.append(float(value[:-2]))
    return res

    

# extract data from w3schools
def extract_data():
    # get page from w3 schools
    request=requests.get(ROOT_URL)

    # extract tabels
    soup=BeautifulSoup(request.text,'html.parser')
    tabels=soup.findAll('table')

    # get browser names
    first_tabel=tabels[0]
    heading=first_tabel.find_all("th")
    browser_names=list(a.string for a in heading[1:])
    db=pd.DataFrame({})

    # create dataframe columns
    columns=["year","month"]
    columns.extend(browser_names)

    # crawl and store data
    for tabel in tabels:
        trs=tabel.find_all("tr")
        year=int(trs[0].find("th").string)
        # check until date is not older than MIN_YEAR
        if year <MIN_YEAR:
            break
        # append data for each month
        for tr in trs:
            tds=tr.find_all("td")
            data=list(a.string for a in tds)
            if len(data)!=len(browser_names)+1:
                continue
            data=clean_data(data)
            if not db.empty:
                db=db.append(create_db_from_data(year,data,columns))
            else :
                db=create_db_from_data(year,data,columns)
    return db
if __name__ == "__main__":
    db = extract_data()
    print(db)
    db.to_csv(FILE_NAME,index=False)