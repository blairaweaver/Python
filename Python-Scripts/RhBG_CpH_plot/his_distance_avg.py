import numpy as np
import matplotlib.pyplot as plt

def filename(n):return '/home/blair/Documents/Mordor/RhBG_Cph/RhBG_ensemble_'+str(n)+'.dat'
def label(n):return "pH = "+str(n+1)
list_of_files = [(filename(x),label(x)) for x in range(0,10,1)]

datalist = [ (np.loadtxt(filename), label ) for filename, label in list_of_files ]
fig, ax = plt.subplots()
n=0
for data, label in datalist:
    avg = np.average(data[:,1])
    std = np.std(data[:,1])
    plt.errorbar(n+1,avg, yerr=std, fmt='o', color="b")
    n= n+1

plt.title("Histidine Distance")
plt.xlabel("pH")
plt.ylabel("Average Distance")
plt.legend(loc="upper right")
plt.xlim([0,11])
#plt.show()
plt.savefig('His_dis_avg.png', bbox_inches='tight')
#help(np.std)
#pylab.title("Title of Plot")
#pylab.xlabel("X Axis Label")
#pylab.ylabel("Y Axis Label")
# print list_of_files
# print label(5)
#pres = pylab.loadtxt("/home/blair/Documents/HPG/RhBG_CpH_modeller/Hold_Analysis/summary.ETOT")
#pylab.plot(pres[:, 0], pres[:, 1], label='pressure')
#pylab.plot(show)
#pylab.show()