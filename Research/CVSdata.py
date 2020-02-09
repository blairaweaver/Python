import pandas as pd
import datetime as dt
import os


def importFile(filename):
    path = os.path.join("Disney Stocks", filename)
    df = pd.read_csv(path)
    return df


def makeDate(data):
    for index, row in data.iterrows():
        data.at[index, 'date'] = dt.datetime.strptime(row['date'], '%m/%d/%Y %H:%M')
    return data


def updateDF(data):
    data['day'] = [dt.datetime.date(d) for d in data['date']]
    data['time'] = [dt.datetime.time(d) for d in data['date']]


May = importFile("1905hfp.csv")
print(May.shape)
print(May.info())
print(May.head())

May = makeDate(May)
print(May.shape)
print(May.info())
print(May.head())

updateDF(May)
print(May.head())

May25 = May[May['day'] == dt.date(year=2019, month=5, day=11)]

print(May25)

for i in range(1,31):
    temp = May[May['day'] == dt.date(year=2019, month=5, day=i)]
    print(temp.tail())