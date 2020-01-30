import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#Functions to return filename
def filename1(n,file):return '/home/blair/Documents/Mordor/'+file+'_Cph/'+file+'_hisn_'+str(n)+'.dat'
def filename2(n,file):return '/home/blair/Documents/Mordor/'+file+'_Cph/'+file+'_his1_di_'+str(n)+'.dat'
def filename3(n,file):return '/home/blair/Documents/Mordor/'+file+'_Cph/'+file+'_his3_di_'+str(n)+'.dat'
def filename4(n,file):return '/home/blair/Documents/Mordor/'+file+'_Cph/'+file+'_his_angle_'+str(n)+'.dat'

#Array with 3 Protein Names
filearray = ["RhAG", "RhBG", "RhCG"]
#Array with Histidine Residue Number (RhAG,RhBG,RhCG)
Residue = ["175","334","186","345","185","344"]
res=0

#Loop through Proteins
for file in filearray:
    #Loop through pH
    for n in range(0,10,1):
        hisDis = np.loadtxt(filename1(n,file))
        hisDiH = np.loadtxt(filename2(n,file))
        hisDiL = np.loadtxt(filename3(n,file))
        hisAng = np.loadtxt(filename4(n,file))
        yarray = hisDiH[:, 1]
        zarray = hisDis[:, 1]
        xarray = hisDiL[:, 1]
        garray = hisAng[:, 1]

        #Create 1st
        fig = plt.figure(figsize=(11.0,10.0))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(xarray, yarray, garray, c='r', marker='o')
        ax.set_ylabel('Dihedral angle of '+Residue[res])
        ax.set_xlabel('Dihedral angle of '+Residue[res+1])
        ax.set_zlabel('His Angle')
        ax.set_xlim3d(-200, 200)
        ax.set_ylim3d(-200, 200)
        ax.set_zlim3d(0, 200)
        ax.set_title(file+"_pH"+str(n+1))
        plt.savefig(file+'_3D_angle_pH'+str(n+1) + '.png', bbox_inches='tight')
        # plt.show()
        plt.close()

        #Create 2nd
        fig = plt.figure(figsize=(11.0,10.0))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(yarray, xarray, garray, c='r', marker='o')
        ax.set_xlabel('Dihedral angle of '+Residue[res])
        ax.set_ylabel('Dihedral angle of '+Residue[res+1])
        ax.set_zlabel('ND1 to ND1 Distance')
        ax.set_xlim3d(-200, 200)
        ax.set_ylim3d(-200, 200)
        ax.set_zlim3d(3, 10)
        ax.set_title(file+"_pH"+str(n+1))
        plt.savefig(file+'_3D_angle_pH'+str(n+1) + '_2.png', bbox_inches='tight')
        # plt.show()
        plt.close()

        #Creates 3rd
        fig = plt.figure(figsize=(11.0,10.0))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(xarray, yarray, zarray, c='r', marker='o')
        ax.set_ylabel('Dihedral angle of '+Residue[res])
        ax.set_xlabel('Dihedral angle of '+Residue[res+1])
        ax.set_zlabel('ND1 to ND1 Distance')
        ax.set_xlim3d(-200, 200)
        ax.set_ylim3d(-200, 200)
        ax.set_zlim3d(3, 10)
        ax.set_title(file+"_pH"+str(n+1))
        plt.savefig(file+'_3D_dih_pH'+str(n+1) + '.png', bbox_inches='tight')
        # plt.show()
        plt.close()

        #Creates 4th
        fig = plt.figure(figsize=(11.0,10.0))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(yarray, xarray, zarray, c='r', marker='o')
        ax.set_xlabel('Dihedral angle of '+Residue[res])
        ax.set_ylabel('Dihedral angle of '+Residue[res+1])
        ax.set_zlabel('His Angle')
        ax.set_xlim3d(-200, 200)
        ax.set_ylim3d(-200, 200)
        ax.set_zlim3d(0, 200)
        ax.set_title(file+"_pH"+str(n+1))
        plt.savefig(file+'_3D_dih_pH'+str(n+1) + '_2.png', bbox_inches='tight')
        # plt.show()
        plt.close()

    res += 2