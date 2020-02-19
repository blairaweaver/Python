import pandas as pd
import datetime as dt
import numpy as np
import os

# pd.options.display.precision

def importFile(filename):
    path = os.path.join("Disney Stocks", filename)
    df = pd.read_csv(path, float_precision='high')
    return df


def makeDate(data):
    for index, row in data.iterrows():
        data.at[index, 'date'] = dt.datetime.strptime(row['date'], '%m/%d/%Y %H:%M')
    return data


def updateDF(data):
    for index, row in data.iterrows():
        data.at[index, 'day'] = dt.datetime.date(row['date'])
        data.at[index, 'time'] = dt.datetime.time(row['date'])
        if not index == 0:
            temp = float(data.at[index, 'close'])
            temp2 = float(data.at[index - 1, 'close'])
            data.at[index, 'diff'] = temp2 - temp

for i in range(5,11):
    temp = importFile("19{:02d}hfp.csv".format(i))
    temp = makeDate(temp)
    updateDF(temp)
    temp_sort = temp.sort_values('close', ascending=False)
    temp_sort.to_csv("test{:02d}sort.csv".format(i))
    temp.to_csv("test{:02d}.csv".format(i))
    # print(i)
    # print(temp.head())


# oct = importFile("1910hfp.csv")
# oct = makeDate(oct)
# May = importFile("1905hfp.csv")
# May.to_csv('AfterImport.csv')
#
# May = makeDate(May)
#
# updateDF(May)
# print(May.head())
#
# print(May.info())
#
#
# May.to_csv('test.csv')
#
