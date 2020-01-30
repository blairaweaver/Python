import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import scipy.stats as st
import matplotlib.ticker as ticker
import matplotlib as mpl

#Functions to return filename
def filename1(n,file):return '/home/blair/Documents/Mordor/'+file+'_Cph/'+file+'_hisn_'+str(n)+'.dat'
def filename2(n):return '/home/blair/Documents/Mordor/RhCG_Conf_Test_2/RhCG_344_di_'+str(n)+'.dat'
def filename3(n):return '/home/blair/Documents/Mordor/RhCG_Conf_Test_2/RhCG_185_di_'+str(n)+'.dat'
def filename4(n):return '/home/blair/Documents/Mordor/RhCG_Conf_Test_2/RhCG_his_angle_'+str(n)+'.dat'
# RhCG_344_di_4.dat

#Function to perform kde
def kde_estimate(x, xmin, xmax, y, ymin, ymax):
    # Peform the kernel density estimate
    xx, yy = np.mgrid[xmin:xmax:200j, ymin:ymax:200j]
    positions = np.vstack([xx.ravel(), yy.ravel()])
    values = np.vstack([x, y])
    kernel = st.gaussian_kde(values)
    f = np.reshape(kernel(positions).T, xx.shape)
    return(xx, yy, f)

#Function to create normalized contour levels from max (used when called before loops and normalizes all 30
# def create_levels():
#     max_values = []
#     # Loop through Proteins
#     for file in filearray:
#         # Loop through pH
#         for n in range(0, 10, 1):
#             # Load Data
#             hisAng = np.loadtxt(filename4(n, file))
#             hisDiH = np.loadtxt(filename2(n, file))
#             hisDiL = np.loadtxt(filename3(n, file))
#             # Chose Column
#             X = hisDiH[:, 1]
#             Z = hisAng[:, 1]
#             Y = hisDiL[:, 1]
#             # Determine Min and Max for kde
#             xmax = max(X)
#             ymin = min(Y)
#             ymax = max(Y)
#             xmin = min(X)
#             zmin = min(Z)
#             zmax = max(Z)
#             # kde with each pair
#             xy, yx, fxy = kde_estimate(X, xmin, xmax, Y, ymin, ymax)
#             xz, zx, fxz = kde_estimate(X, xmin, xmax, Z, zmin, zmax)
#             yz, zy, fyz = kde_estimate(Y, ymin, ymax, Z, zmin, zmax)
#             max_values.append(np.amax(fxz))
#             max_values.append(np.amax(fxy))
#             max_values.append(np.amax(fyz))
#     f_max = min(max_values)
#     levels = np.linspace(0,1,num=50)
#     return levels, f_max

def create_levels():
    max_values = []
    # Loop through pH
    for n in range(4, 8, 1):
        # Load Data
        hisAng = np.loadtxt(filename4(n))
        hisDiH = np.loadtxt(filename2(n))
        hisDiL = np.loadtxt(filename3(n))
        # Chose Column
        X = hisDiH[:, 1]
        Z = hisAng[:, 1]
        Y = hisDiL[:, 1]
        # Determine Min and Max for kde
        xmax = max(X)
        ymin = min(Y)
        ymax = max(Y)
        xmin = min(X)
        zmin = min(Z)
        zmax = max(Z)
        # kde with each pair
        xy, yx, fxy = kde_estimate(X, xmin, xmax, Y, ymin, ymax)
        xz, zx, fxz = kde_estimate(X, xmin, xmax, Z, zmin, zmax)
        yz, zy, fyz = kde_estimate(Y, ymin, ymax, Z, zmin, zmax)
        max_values.append(np.amax(fxz))
        max_values.append(np.amax(fxy))
        max_values.append(np.amax(fyz))
    f_max = max(max_values)
    levels = np.linspace(0,1,num=50)
    return levels, f_max

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
levels, f_max = create_levels()
for n in range(0,10,1):
    #Load Data
    hisAng = np.loadtxt(filename4(n))
    hisDiH = np.loadtxt(filename2(n))
    hisDiL = np.loadtxt(filename3(n))
    #Chose Column
    Y = hisDiH[:, 1]
    Z = hisAng[:, 1]
    X = hisDiL[:, 1]
    #Give data in order to have contour cover entire 3D graph
    diAppend = [-180, 180]
    anAppend = [0, 180]
    X = np.append(X, diAppend)
    Y = np.append(Y, diAppend)
    Z = np.append(Z, anAppend)
    #Determine Min and Max for kde
    xmax = max(X)
    ymin = min(Y)
    ymax = max(Y)
    xmin = min(X)
    zmin = min(Z)
    zmax = max(Z)
    #kde with each pair
    xy, yx, fxy = kde_estimate(X, xmin, xmax, Y, ymin, ymax)
    xz, zx, fxz = kde_estimate(X, xmin, xmax, Z, zmin, zmax)
    yz, zy, fyz = kde_estimate(Y, ymin, ymax, Z, zmin, zmax)
    #create levels for contour
    # levels, f_max = create_levels(fxy,fxz,fyz)
    fig = plt.figure(figsize=(13.5,10.0))
    plt.style.use('seaborn-white')
    ax = fig.add_subplot(111, projection='3d')
    #Plot each contour and offset to plane
    cset = ax.contourf(xy, yx, fxy/f_max, levels, zdir='z', offset=-0,cmap=cm.terrain)
    cset = ax.contourf(xz, fxz/f_max, zx, levels, zdir='y', offset=200, cmap=cm.terrain)
    cset = ax.contourf(fyz/f_max, yz, zy, levels, zdir='x', offset=-200, cmap=cm.terrain)
    #plot the colorbar, format converts number to scientific, shrink is length of colorbar, aspect is width
    cbar = plt.colorbar(cset, shrink=0.6) #format=ticker.FuncFormatter(fmt)
    cbar.ax.set_ylabel('Density')
    #axes for graph
    ax.set_xlabel('Dihedral of Residue 344 ($^\circ$)',labelpad=10)
    ax.set_ylabel('Dihedral of Residue 185 ($^\circ$)',labelpad=10)
    ax.set_zlabel('Angle Between Residue 185 and 344 ($^\circ$)',labelpad=10)
    ax.set_xlim3d(-200, 200)
    ax.set_ylim3d(-200, 200)
    ax.set_zlim3d(0, 200)
    ax.set_title("RhCG at pH"+str(n+1))
    # plt.savefig('/home/blair/Documents/Graphs/3D/'+file+'_3D_angle_contour_pH'+str(n+1) +'_percent_4.png', bbox_inches='tight')
    plt.savefig('/home/blair/Documents/temp/RhCG_Conf_3D_angle_contour_pH' + str(n + 1) + '_percent_test_1.png',bbox_inches='tight')
    # plt.show()
    plt.close()
