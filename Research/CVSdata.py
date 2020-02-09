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
        data['diff'] = 1.000000005
        data.to_numpy()

    print(data.info())
    for index, row in data.iterrows():
        if not index == 0:
            temp = data.at[index, 'close']
            temp2 = data.at[index - 1, 'close']
            print(round(temp - temp2, 4))

            data['diff'] = round(temp - temp2, 4)


May = importFile("1905hfp.csv")
May.to_csv('AfterImport.csv')

May = makeDate(May)

updateDF(May)
print(May.head())

print(May.info())


May.to_csv('test.csv')

