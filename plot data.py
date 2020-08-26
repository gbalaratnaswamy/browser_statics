import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from cfg import FILE_NAME

db=pd.read_csv(FILE_NAME)

# function to plot data
def plot_data(browser_name):
    data=db[browser_name].to_numpy(dtype=float)
    plt.plot(data)
    plt.show()

plot_data("Opera")