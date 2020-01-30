import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

#Functions to return filename
# def filename1(n,file):return '/home/blair/Documents/Mordor/'+file+'_Cph/'+file+'_rmsf_'+str(n)+'.dat'
def filename1(n,file):return '/home/blair/Documents/Mordor/'+file+'_Trimer/'+file+'_rmsf_'+str(n)+'.dat'

Protein = ["RhAG", "RhBG", "RhCG"]
fig, ax = plt.subplots()
for m in Protein:
    for n in range(0, 10, 1):
        rmsf = np.loadtxt(filename1(n,m))
        yarray = rmsf[:, 1]
        xarray = rmsf[:, 0]
        xmin = 0
        xmax = max(xarray)
        ymin = min(yarray)
        ymax = max(yarray)
        plt.figure(figsize=(13.5, 10.0))
        plt.xlim(0, xmax)
        plt.ylim(0, 15)
        plt.plot(xarray, yarray)
        plt.title("RMSF of "+m+" at pH"+str(n+1))
        plt.xlabel("Residue")
        plt.ylabel("RMSF")
        plt.legend(loc="upper right")
        # plt.show()
        plt.savefig('/home/blair/Documents/temp/'+m+'_rmsf_Trimer_pH'+str(n+1) + '.png', bbox_inches='tight')
        plt.close()