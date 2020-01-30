import numpy as np
import matplotlib.pyplot as plt

def filename(n):return '/home/blair/Documents/Mordor/RhAG_Cph/RhAG_rmsd_'+str(n)+'.dat'
def label(n):return "pH = "+str(n+1)
list_of_files = [(filename(x),label(x)) for x in range(0,10,1)]

datalist = [ ( np.loadtxt(filename), label ) for filename, label in list_of_files ]
fig, ax = plt.subplots()
n=0
for data, label in datalist:
    avg = np.average(data[:,1])
    std = np.std(data[:,1])
    plt.errorbar(n+1,avg, yerr=std)
    n= n+1

plt.title("rms average")
plt.xlabel("Frames")
plt.ylabel("rms")
plt.legend(loc="upper right")
plt.xlim([0,11])
plt.show()