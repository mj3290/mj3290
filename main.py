import pandas_datareader as web
import pandas_datareader as pd
import datetime

from pandas.tools.plotting import scatter_matrix

def download_data(filename, comcode, y1, m1, d1, y2, m2, d2):
    start = datetime.datetime(y1, m1, m1)
    end = datetime.datetime(y2, m2, m2)
    df = web.DataReader("%s.KS" % (comcode), "yahoo", start, end)
    df.to_pickle(filename)
    return df



def main():
    df = download_data("data.txt", "005930", 2015,1,1,2015,11,30)
    print df.describe()
    df[['Open', 'High', 'Low', 'Close']].plot(kind='box')
    plot.show()

main()