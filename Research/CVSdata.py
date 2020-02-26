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

# This can open all the files at once and does some data processing
# for i in range(5,11):
#     temp = importFile("19{:02d}hfp.csv".format(i))
#     temp = makeDate(temp)
#     updateDF(temp)
#     temp_sort = temp.sort_values('close', ascending=False)
#     temp_sort.to_csv("test{:02d}sort.csv".format(i))
#     temp.to_csv("test{:02d}.csv".format(i))
# print(i)
# print(temp.head())


# oct = importFile("1910hfp.csv")
# oct = makeDate(oct)
May = importFile("fakedata.csv")
# May.to_csv('AfterImport.csv')

May = makeDate(May)

updateDF(May)
May_Day1 = May[May['day'] == dt.date(2019, 5, 1)]
print(May_Day1.head())
print(May_Day1.max())
print(May_Day1['close'].max())
May_Day1_Max = May_Day1[May_Day1['close']==May_Day1['close'].max()]
print(May_Day1_Max.head())


for idx in reversed(May_Day1_Max.index):
    print(idx)
    print(May_Day1_Max.at[idx, 'time'])


# This sort doesn't preserve the time sort.
# May_Day1_sort = May_Day1.sort_values('close', ascending=False)
# print(May_Day1_sort.head())

# Need to pull all with the max and then sort by time
# for index, row in May_Day1_sort.iterrows():
#     print()

# May_Day1.to_csv('FakeDay1unsorted.csv')
# May_Day1_sort.to_csv('FakeDay1sorted.csv')
# May_Day1_Max.to_csv('FakeMax.csv')
# print(May.head())
# print(May.info())
# May.to_csv('test.csv')
#
