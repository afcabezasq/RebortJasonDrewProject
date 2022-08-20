import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal

def preprocessing():
    data_set = pd.read_csv('archives/archive/AEP_hourly.csv')
    y = np.array(data_set.AEP_MW)
    date_array = pd.to_datetime(data_set.Datetime)
    plt.plot(date_array, y)

    plt.plot(date_array, y)
    plt.xlabel("Date", fontsize=15)
    plt.ylabel("MW Energy Consumption", fontsize=15)
    plt.show()
    return y, date_array


def main():
    y, date_array = preprocessing()

if __name__ == "__main__":
    main()