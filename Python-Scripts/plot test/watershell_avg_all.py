import numpy as np
import matplotlib.pyplot as plt
def filenameA(n):return '/home/blair/Documents/Mordor/RhAG_Cph/RhAG_watershell_'+str(n)+'.dat'
def filenameB(n):return '/home/blair/Documents/Mordor/RhBG_Cph/RhBG_watershell_'+str(n)+'.dat'
def filenameC(n):return '/home/blair/Documents/Mordor/RhCG_Cph/RhCG_watershell_'+str(n)+'.dat'
def labelV(n):return "pH = "+str(n+1)


list_of_filesC = [(filenameC(x),labelV(x)) for x in range(0,10,1)]
datalistC = [ (np.loadtxt(filenameC), labelC) for filenameC, labelC in list_of_filesC ]
fig, ax = plt.subplots()
arrayC_avg=[]
arrayC_std=[]
n=0
for data, label in datalistC:
    avg = np.average(data[:,2])
    std = np.std(data[:,2])
    arrayC_avg.append(avg)
    arrayC_std.append(std)
    n= n+1


list_of_filesA = [(filenameA(x),labelV(x)) for x in range(0,10,1)]
datalistA = [ (np.loadtxt(filenameA), labelA) for filenameA, labelA in list_of_filesA ]
arrayA_avg=[]
arrayA_std=[]
n=0
for data, label in datalistA:
    avg = np.average(data[:,2])
    std = np.std(data[:,2])
    arrayA_avg.append(avg)
    arrayA_std.append(std)
    n= n+1



list_of_filesB = [(filenameB(x),labelV(x)) for x in range(0,10,1)]
datalistB = [ (np.loadtxt(filenameB), labelB) for filenameB, labelB in list_of_filesB]
arrayB_avg=[]
arrayB_std=[]
n=0
for data, label in datalistB:
    avg = np.average(data[:,2])
    std = np.std(data[:,2])
    arrayB_avg.append(avg)
    arrayB_std.append(std)
    n= n+1
xlabel = [x for x in range(1,11,1)]

plt.errorbar(xlabel,arrayA_avg, yerr=arrayA_std, fmt='o', color="r", label="RhAG")
plt.errorbar(xlabel, arrayB_avg, yerr=arrayB_std, fmt='o', color="b", label="RhBG")
plt.errorbar(xlabel,arrayC_avg, yerr=arrayC_std, fmt='o', color="g", label="RhCG")

plt.title("Number of Water within 5.0")
plt.xlabel("pH")
plt.ylabel("Number")
plt.legend(loc="upper right", numpoints=1)
plt.xlim([0,11])
#plt.show()
plt.savefig('Watershell_avg_all.png', bbox_inches='tight')
