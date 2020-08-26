# this is a command line app to fetch and plot data
# 

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
import sys
from cfg import *
from main import extract_data
from plot_data import plot_data
arguments=sys.argv
file_path=arguments[0]

# get command
try :
    command=arguments[1]
# if command not given
except:
    print("error occured")
    sys.exit()

# if user requests to fetch data from w3schools website
if command=="fetch":
    db=extract_data()
    db.to_csv(FILE_NAME,index=False)
    print("fetch sucess")
    print(db)
elif command=="set":
    pass
elif command=="get":
    pass
elif command=="plot_data":
    try:
        plot_data(arguments[2])
    except:
        print("invalid browser name try one of these")
        db=pd.read_csv(FILE_NAME)
        for col in db.columns[2:]:
            print(col)


