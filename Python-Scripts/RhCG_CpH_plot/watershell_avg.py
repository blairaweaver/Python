import numpy as np
import matplotlib.pyplot as plt

def filename(n):return '/home/blair/Documents/Mordor/RhCG_Cph/RhCG_watershell_'+str(n)+'.dat'
def label(n):return "pH = "+str(n+1)
list_of_files = [(filename(x),label(x)) for x in range(0,10,1)]

datalist = [ (np.loadtxt(filename), label ) for filename, label in list_of_files ]
fig, ax = plt.subplots()
n=0
for data, label in datalist:
    avg = np.average(data[:,2])
    std = np.std(data[:,2])
    plt.errorbar(n+1,avg, yerr=std, fmt='o', color="b")
    n= n+1

plt.title("Number of Water within 5.0")
plt.xlabel("pH")
plt.ylabel("Number")
plt.legend(loc="upper right")
plt.xlim([0,11])
#plt.show()
plt.savefig('Watershell_avg.png', bbox_inches='tight')