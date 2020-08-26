import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from cfg import FILE_NAME


# function to plot data
def plot_data(browser_name):
    db=pd.read_csv(FILE_NAME)
    data=db[browser_name].to_numpy(dtype=float)
    plt.plot(data)
    plt.show()

if __name__ == "__main__":
    plot_data("Opera")