import pandas as pd
import datetime as dt
import numpy as np
import os
import calendar as cal
import matplotlib.pyplot as plt


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
for i in range(5, 11):
    fullData = importFile("19{:02d}hfp.csv".format(i))
    fullData = makeDate(fullData)
    updateDF(fullData)
    #     temp_sort = temp.sort_values('close', ascending=False)
    #     temp_sort.to_csv("test{:02d}sort.csv".format(i))
    #     temp.to_csv("test{:02d}.csv".format(i))
    #     Cycle through all the days in the month
    for j in range(1, cal.monthrange(2019, i)[1] + 1):
        # if weekend, skip to next day (doesn't catch holidays :'( )
        if (dt.date(2019, i, j).weekday() >= 5):
            continue
        print(dt.date(2019, i, j))
        DayValues = fullData[fullData['day'] == dt.date(2019, i, j)]
        # Checks for holidays
        if DayValues.empty:
            continue
        print(DayValues.head())
        DayMaxValues = DayValues[DayValues['close'] == DayValues['close'].max()]
        print(DayValues['close'].max())
        DaySegments = []
        endindex = DayValues.last_valid_index() + 1 - DayValues.index[0]
        for idx in reversed(DayMaxValues.index):
            temp = idx - DayValues.index[0]
            print(DayValues.index)
            print(DayValues.iloc[temp:endindex, :])
            DaySegments.append(DayValues.iloc[temp:endindex, :])
            endindex = temp
        if endindex > 0:
            # df.at[4, 'B']
            print(DayValues.iloc[0:endindex, :])
            DaySegments.append(DayValues.iloc[0:endindex, :])
        for x in range(0, len(DaySegments)):
            DaySegments[x].to_csv("test{:02d}_{:02d}_{:02d}.csv".format(i, j, len(DaySegments) - x))
            DaySegments[x].plot(x = 'time', y = 'close', kind = 'line')
            plt.savefig("test{:02d}_{:02d}_{:02d}.png".format(i, j, len(DaySegments) - x))
            plt.close()
            plt.plot_date(DaySegments[x]['time'], DaySegments[x]['close'])
            plt.savefig("test{:02d}_{:02d}_{:02d}_scatter.png".format(i, j, len(DaySegments) - x))
            plt.close()
            # plt.show()
            # print()

# print(i)
# print(temp.head())
# for i in range(5,11):
#     for j in range(1, cal.monthrange(2019, i)[1] + 1):
#         print(dt.date(2019, i, j))
#         print(dt.date(2019, i, j).weekday() >= 5)


# oct = importFile("1910hfp.csv")
# oct = makeDate(oct)

# May.to_csv('AfterImport.csv')

# From this comment to the Comment labeled "STOP" does the segmentation on fakedate file
# May = importFile("fakedata.csv")
# May = makeDate(May)
#
# updateDF(May)
#
# May_Day1 = May[May['day'] == dt.date(2019, 5, 2)]
# print(May_Day1.head())
# print(May_Day1['close'].max())
# May_Day1_Max = May_Day1[May_Day1['close']==May_Day1['close'].max()]
# print(May_Day1_Max.head())
#
# Day1Segments = []
# endindex = May_Day1.last_valid_index() - May_Day1.index[0]
# for idx in reversed(May_Day1_Max.index):
#     temp = idx - May_Day1.index[0]
#     # print(endindex)
#     # print(idx)
#     # print(May_Day1_Max.at[idx, 'time'])
#     print("{0}, {1}".format(temp, endindex))
#     print(May_Day1.iloc[temp:endindex, :])
#     print(May_Day1.iloc[0:200, :])
#     # print(May_Day1.iloc[idx:endindex, :])
#     Day1Segments.append(May_Day1.iloc[temp:endindex, :])
#     endindex = temp - 1
# print(endindex)
# print(May_Day1.index[0])
# print(May_Day1.index)
# if endindex > 0:
#     print(May_Day1.iloc[0:endindex, :])
#     Day1Segments.append(May_Day1.iloc[0:endindex, :])
#
# print(Day1Segments[-1].head())
# print(May_Day1['date'].iloc[-1])
# print(May_Day1.last_valid_index())

# "STOP"

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
