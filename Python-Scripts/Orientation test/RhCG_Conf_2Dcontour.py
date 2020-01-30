import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import scipy.stats as st
import matplotlib.ticker as ticker
import matplotlib as mpl

#Functions to return filename
def filename1(n,file):return '/home/blair/Documents/Mordor/'+file+'_Cph/'+file+'_hisn_'+str(n)+'.dat'
def filename2(n, residue, run):return '/home/blair/Extra/Mordor/RhCG_Conf_Test_2/RhCG_'+str(residue)+'_di_'+run+'_'+str(n)+'.dat'
def filename3(n, residue):return '/home/blair/Extra/Mordor/RhCG_Conf_Test_2/RhCG_'+str(residue)+'_di_'+str(n)+'.dat'
def filename4(n):return '/home/blair/Documents/Mordor/RhCG_Conf_Test_2/RhCG_his_angle_'+str(n)+'.dat'
# RhCG_344_di_4.dat
# RhCG_185_di_Phe_4.dat
# RhCG_235_di_Phe_3.dat
# RhCG_344_di_Phe_1.dat

# Formatting taken from http://stackoverflow.com/questions/25983218/
def fmt(x, pos):
    a, b = '{:.2e}'.format(x).split('e')
    b = int(b)
    return r'${} \times 10^{{{}}}$'.format(a, b)


#Array with Histidine Residue Number (RhAG,RhBG,RhCG)
Residue = ["185","344"]


mpl.rc('axes', fc='white') #Does this do anything?
# levels, f_max = create_levels()


#Loop through pH
Restraint = ['Phe', 'His']
Residue = [344, 235, 185]
fig, ax = plt.subplots()
#for when there is one restraint still active
# for i in Restraint:
#     for m in Residue:
#         for n in range(0, 10, 1):
#             hisLoop = np.loadtxt(filename2(n, m, i))
#             yarray = hisLoop[:, 1]
#             xarray = hisLoop[:, 0]
#             xmin = 0
#             xmax = max(xarray)
#             ymin = min(yarray)
#             ymax = max(yarray)
#             plt.xlim(0, xmax)
#             plt.ylim(-200, 200)
#             plt.scatter(xarray, yarray)
#             plt.title("Dihedral of Residue "+str(m)+" vs Frame for RhCG at pH"+str(n+1))
#             plt.xlabel("Frame")
#             plt.ylabel("Dihedral of Residue "+str(m))
#             plt.legend(loc="upper right")
#             # plt.show()
#             plt.savefig('/home/blair/Documents/temp/RhCG_di_'+i+str(m)+'_pH'+str(n+1) + '.png', bbox_inches='tight')
#             plt.close()

#for when there is no restraint
for m in Residue:
    for n in range(0, 10, 1):
        hisLoop = np.loadtxt(filename3(n, m))
        yarray = hisLoop[:, 1]
        xarray = hisLoop[:, 0]
        xmin = 0
        xmax = max(xarray)
        ymin = min(yarray)
        ymax = max(yarray)
        plt.xlim(0, xmax)
        plt.ylim(-200, 200)
        plt.scatter(xarray, yarray)
        plt.title("Dihedral of Residue "+str(m)+" vs Frame for RhCG at pH"+str(n+1))
        plt.xlabel("Frame")
        plt.ylabel("Dihedral of Residue "+str(m))
        plt.legend(loc="upper right")
        # plt.show()
        plt.savefig('/home/blair/Documents/temp/RhCG_di_nores_'+str(m)+'_pH'+str(n+1) + '.png', bbox_inches='tight')
        plt.close()