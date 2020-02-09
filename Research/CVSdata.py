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
    for d in data['date']:
        data['day'] = dt.datetime.date(d)
        data['time'] = dt.datetime.time(d)

    print(data.info())
    for index, row in data.iterrows():
        if not index == 0:
            temp = float(data.at[index, 'close'])
            print(temp)
            temp2 = float(data.at[index - 1, 'close'])
            temp3 = str(temp2 - temp)
            data['diff'] = temp3


May = importFile("1905hfp.csv")
May.to_csv('AfterImport.csv')

May = makeDate(May)

updateDF(May)
print(May.head())

print(May.info())


May.to_csv('test.csv')

