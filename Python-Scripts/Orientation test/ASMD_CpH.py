import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

def filename1():return '/home/blair/Extra/Mordor/ASMD_CpH_Test_10/pmemd_dat/jar.pmemd.dat'
def filename2():return '/home/blair/Extra/Mordor/ASMD_CpH_Test_10/sander_dat/jar.sander.dat'
def filename3(n):return '/home/blair/Extra/Mordor/ASMD_CpH_Test_10/ASMD_sander_'+str(n)+'.work.dat.1'
def findmax():
    all_x_values = []
    all_y_values = []
    for i in range (1,23,1):
        swork=np.loadtxt(filename3(i))
        xarray=swork[:,0]
        yarray=swork[:,3]
        all_x_values.append(xarray)
        all_y_values.append(yarray)
    ymax = np.amax(all_y_values)
    ymin = np.amin(all_y_values)
    xmax = np.amax(all_x_values)
    xmin = np.amin(all_x_values)
    return ymax, ymin, xmax, xmin



pmemd=np.loadtxt(filename1())
sander=np.loadtxt(filename2())


pyarray = pmemd[:, 1]
pxarray = pmemd[:, 0]
syarray = sander[:,1]
sxarray = sander[:,0]
ymax, ymin, xmax, xmin = findmax()
# xmin = min(sxarray)
# xmax = max(sxarray)
# ymin = min(syarray)
# ymax = max(pyarray)
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.scatter(sxarray, syarray, c="b", label="sander")
plt.scatter(pxarray, pyarray, c="r", label="pmemd")
for i in range (1,23,1):
    swork=np.loadtxt(filename3(i))
    xarray=swork[:,0]
    yarray=swork[:,3]
    string = 'swork' + str(i)
    plt.scatter(xarray,yarray, label=string)
plt.title("pmemd vs sander on ASMD and CpH")
plt.xlabel("Distance")
plt.ylabel("PMF")
plt.legend(loc="upper right")
plt.show()
# plt.savefig('/home/blair/Documents/temp/pmemd_vs_sander.png', bbox_inches='tight')
plt.close()