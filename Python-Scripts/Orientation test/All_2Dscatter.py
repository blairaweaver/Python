import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
##OLD FILENAMES NEED TO UPDATE CODE!!!!!
# def filenameA(n):return '/home/blair/Documents/Mordor/RhAG_Cph/RhAG_hisn_'+str(n)+'.dat'
# def filenameA2(n):return '/home/blair/Documents/Mordor/RhAG_Cph/RhAG_175_di_'+str(n)+'.dat'
# def filenameA3(n):return '/home/blair/Documents/Mordor/RhAG_Cph/RhAG_334_di_'+str(n)+'.dat'
# def filenameA4(n):return '/home/blair/Documents/Mordor/RhAG_Cph/RhAG_his_angle_'+str(n)+'.dat'
# def filenameA5(n):return '/home/blair/Documents/Mordor/RhAG_Cph/RhAG_loop1_'+str(n)+'.dat'
# def filenameA6(n):return '/home/blair/Documents/Mordor/RhAG_Cph/RhAG_loop2_'+str(n)+'.dat'
# def filenameA7(n):return '/home/blair/Documents/Mordor/RhAG_Cph/RhAG_334_di_chi1_'+str(n)+'.dat'
# def filenameA8(m,n):return '/home/blair/Documents/Mordor/RhAG_Cph/RhAG_dis'+str(m)+'_'+str(n)+'.dat'
# def filenameA9(m,n):return '/home/blair/Documents/Mordor/RhAG_Cph/RhAG_di'+str(m)+'_'+str(n)+'.dat'
# def filenameA10(m):return '/home/blair/Documents/Mordor/RhAG_Cph/RhAG_rmsf_'+str(m)+'.dat'
#
# def filenameB(n):return '/home/blair/Documents/Mordor/RhBG_Cph/RhBG_hisn_'+str(n)+'.dat'
# def filenameB2(n):return '/home/blair/Documents/Mordor/RhBG_Cph/RhBG_186_di_'+str(n)+'.dat'
# def filenameB3(n):return '/home/blair/Documents/Mordor/RhBG_Cph/RhBG_345_di_'+str(n)+'.dat'
# def filenameB4(n):return '/home/blair/Documents/Mordor/RhBG_Cph/RhBG_his_angle_'+str(n)+'.dat'
# def filenameB5(m):return '/home/blair/Documents/Mordor/RhBG_Cph/RhBG_rmsf_'+str(m)+'.dat'
#
# def filenameC(n):return '/home/blair/Documents/Mordor/RhCG_Cph/RhCG_hisn_'+str(n)+'.dat'
# def filenameC2(n):return '/home/blair/Documents/Mordor/RhCG_Cph/RhCG_185_di_'+str(n)+'.dat'
# def filenameC3(n):return '/home/blair/Documents/Mordor/RhCG_Cph/RhCG_344_di_'+str(n)+'.dat'
# def filenameC4(n):return '/home/blair/Documents/Mordor/RhCG_Cph/RhCG_his_angle_'+str(n)+'.dat'
# def filenameC5(m):return '/home/blair/Documents/Mordor/RhCG_Cph/RhCG_rmsf_'+str(m)+'.dat'

#Functions to return filename
def filename1(n,file):return '/home/blair/Documents/Mordor/'+file+'_Cph/'+file+'_hisn_'+str(n)+'.dat'
def filename2(n,file):return '/home/blair/Documents/Mordor/'+file+'_Cph/'+file+'_his1_di_'+str(n)+'.dat'
def filename3(n,file):return '/home/blair/Documents/Mordor/'+file+'_Cph/'+file+'_his3_di_'+str(n)+'.dat'
def filename4(n,file):return '/home/blair/Documents/Mordor/'+file+'_Cph/'+file+'_his_angle_'+str(n)+'.dat'

def filename5(n,m):return '/home/blair/Documents/Mordor/RhCG_Conf_Test_2/RhCG_'+str(n)+'_di_'+str(m)+'.dat'

#Function to perform kde
def kde_estimate(x, xmin, xmax, y, ymin, ymax):
    # Peform the kernel density estimate
    xx, yy = np.mgrid[xmin:xmax:200j, ymin:ymax:200j]
    positions = np.vstack([xx.ravel(), yy.ravel()])
    values = np.vstack([x, y])
    kernel = st.gaussian_kde(values)
    f = np.reshape(kernel(positions).T, xx.shape)
    return(xx, yy, f)

#Function to create contour levels from min and max
def create_levels(f1, f2, f3):
    max_values = [np.amax(f1),np.amax(f2),np.amax(f3)]
    f_max = max(max_values)
    levels = np.linspace(0,f_max,num=40)
    return levels

# Formatting taken from http://stackoverflow.com/questions/25983218/
def fmt(x, pos):
    a, b = '{:.2e}'.format(x).split('e')
    b = int(b)
    return r'${} \times 10^{{{}}}$'.format(a, b)

##rmsf plots

# for n in range(0,10,1):
#     hisAng = np.loadtxt(filenameA10(n))
#     # xarray = hisAng[:, 0]
#     # yarray = hisAng[:, 1]
#     # plt.scatter(xarray, yarray)
#     plt.figure(figsize=(12,9))
#     plt.plot(hisAng[:,0],hisAng[:,1])
#     plt.title("Fluctuation vs Residue for RhAG at pH"+str(n+1))
#     plt.xlim(0, 450)
#     plt.ylim(0, 15)
#     plt.xlabel("Residue")
#     plt.ylabel("Fluctuation")
#     plt.legend(loc="upper right")
#     # fig_size = []
#     # fig_size[0] = 12
#     # fig_size[1] = 9
#     # plt.rcParams["figure.figsize"] = plt.fig_size
#     #plt.show()
#     plt.savefig('RhAG_rmsf_pH'+str(n+1) + '.png', dpi= 200, bbox_inches='tight')
#     plt.close()

# for n in range(0, 10, 1):
#     hisAng = np.loadtxt(filenameB5(n))
#     # xarray = hisAng[:, 0]
#     # yarray = hisAng[:, 1]
#     # plt.scatter(xarray, yarray)
#     plt.figure(figsize=(12, 9))
#     plt.plot(hisAng[:, 0], hisAng[:, 1])
#     plt.title("Fluctuation vs Residue for RhBG at pH" + str(n + 1))
#     plt.xlim(0, 450)
#     plt.ylim(0, 15)
#     plt.xlabel("Residue")
#     plt.ylabel("Fluctuation")
#     plt.legend(loc="upper right")
#     # fig_size = []
#     # fig_size[0] = 12
#     # fig_size[1] = 9
#     # plt.rcParams["figure.figsize"] = plt.fig_size
#     # plt.show()
#     plt.savefig('RhBG_rmsf_pH' + str(n + 1) + '.png', dpi=200, bbox_inches='tight')
#     plt.close()
#
# for n in range(0, 10, 1):
#     hisAng = np.loadtxt(filenameC5(n))
#     # xarray = hisAng[:, 0]
#     # yarray = hisAng[:, 1]
#     # plt.scatter(xarray, yarray)
#     plt.figure(figsize=(12, 9))
#     plt.plot(hisAng[:, 0], hisAng[:, 1])
#     plt.title("Fluctuation vs Residue for RhCG at pH" + str(n + 1))
#     plt.xlim(0, 450)
#     plt.ylim(0, 15)
#     plt.xlabel("Residue")
#     plt.ylabel("Fluctuation")
#     plt.legend(loc="upper right")
#     # fig_size = []
#     # fig_size[0] = 12
#     # fig_size[1] = 9
#     # plt.rcParams["figure.figsize"] = plt.fig_size
#     # plt.show()
#     plt.savefig('RhCG_rmsf_pH' + str(n + 1) + '.png', dpi=200, bbox_inches='tight')
#     plt.close()


# Contour Plot
def kde_estimate(x, xmin, xmax, y, ymin, ymax):
    # Peform the kernel density estimate
    xx, yy = np.mgrid[xmin:xmax:200j, ymin:ymax:200j]
    positions = np.vstack([xx.ravel(), yy.ravel()])
    values = np.vstack([x, y])
    kernel = st.gaussian_kde(values)
    f = np.reshape(kernel(positions).T, xx.shape)
    return(xx, yy, f)

Residue = [344, 235, 185]
fig, ax = plt.subplots()
for m in Residue:
    for n in range(0, 10, 1):
        hisLoop = np.loadtxt(filename5(m, n))
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
        plt.savefig('/home/blair/Documents/temp/RhCG_di_'+str(m)+'_pH'+str(n+1) + '.png', bbox_inches='tight')
        plt.close()






# fig, ax = plt.subplots()
# for n in range(0,10,1):
#     for m in range(1,7,1):
#         hisLoop = np.loadtxt(filenameA8(m,n))
#         hisChi = np.loadtxt(filenameA7(n))
#         xarray = hisLoop[:, 1]
#         yarray = hisChi[:, 1]
#         xmin = 0
#         xmax = max(xarray)
#         ymin = min(yarray)
#         ymax = max(yarray)
#         xx, yy, f = kde_estimate(xarray, xmin, xmax, yarray, ymin, ymax)
#         # plt.xlim(0, 25)
#         # plt.ylim(-200, 200)
#         cfset = plt.contourf(xx, yy, f, cmap='BuGn')
#         #plt.scatter(xarray, yarray)
#         plt.title("Distance "+str(m)+" vs Histidine 334 Conformation for RhAG at pH" + str(n + 1))
#         plt.xlabel("Distance")
#         plt.ylabel("Chi 1 of Histidine 334")
#         plt.legend(loc="upper right")
#         #plt.show()
#         plt.savefig('RhAG_chi_dis'+str(m)+'_pH' + str(n + 1) + '_con.png', bbox_inches='tight')
#         plt.close()
    # for m in range(1,6,1):
    #     hisLoop = np.loadtxt(filenameA9(m,n))
    #     hisChi = np.loadtxt(filenameA7(n))
    #     xarray = hisLoop[:, 1]
    #     yarray = hisChi[:, 1]
    #     xmin = min(xarray)
    #     xmax = max(xarray)
    #     ymin = min(yarray)
    #     ymax = max(yarray)
    #     xx, yy, f = kde_estimate(xarray, xmin, xmax, yarray, ymin, ymax)
    #     # plt.xlim(-200, 200)
    #     # plt.ylim(-200, 200)
    #     cfset = plt.contourf(xx, yy, f, cmap='BuGn')
    #     #plt.scatter(xarray, yarray)
    #     plt.title("Dihedral "+str(m)+" vs Histidine 334 Conformation for RhAG at pH" + str(n + 1))
    #     plt.xlabel("Dihedral")
    #     plt.ylabel("Chi 1 of Histidine 334")
    #     plt.legend(loc="upper right")
    #     #plt.show()
    #     plt.savefig('RhAG_chi_di'+str(m)+'_pH' + str(n + 1) + '_con.png', bbox_inches='tight')
    #     plt.close()
    # for m in range(1, 6, 1):
    #     hisLoop = np.loadtxt(filenameA9(m, n))
    #     hisChi = np.loadtxt(filenameA7(n))
    #     xarray = hisLoop[:, 1]
    #     yarray = hisChi[:, 1]
    #     # plt.xlim(-200, 200)
    #     # plt.ylim(-200, 200)
    #     plt.scatter(xarray, yarray)
    #     plt.title("Dihedral " + str(m) + " vs Histidine 334 Conformation for RhAG at pH" + str(n + 1))
    #     plt.xlabel("Dihedral")
    #     plt.ylabel("Chi 1 of Histidine 334")
    #     plt.legend(loc="upper right")
    #     #plt.show()
    #     plt.savefig('RhAG_chi_di' + str(m) + '_pH' + str(n + 1) + '.png', bbox_inches='tight')
    #     plt.close()
    #
    # for m in range(1,7,1):
    #     hisChi = np.loadtxt(filenameA7(n))
    #     hisLoop = np.loadtxt(filenameA8(m,n))
    #     xarray = hisLoop[:, 1]
    #     yarray = hisChi[:, 1]
    #     # plt.xlim(0, 25)
    #     # plt.ylim(-200, 200)
    #     plt.scatter(xarray, yarray)
    #     plt.title("Distance "+str(m)+" vs Histidine 334 Conformation for RhAG at pH" + str(n + 1))
    #     plt.xlabel("Distance")
    #     plt.ylabel("Chi 1 of Histidine 334")
    #     plt.legend(loc="upper right")
    #     # plt.show()
    #     plt.savefig('RhAG_chi_dis'+str(m)+'_pH' + str(n + 1) + '.png', bbox_inches='tight')
    #     plt.close()

    #
    # hisChi = np.loadtxt(filenameA3(n))
    # hisLoop = np.loadtxt(filenameA6(n))
    # xarray = hisLoop[:, 1]
    # yarray = hisChi[:, 1]
    # plt.scatter(xarray, yarray)
    # plt.title("Loop Conformation vs Histidine 334 Conformation for RhAG at pH"+str(n+1))
    # plt.xlabel("Distance between Residue 43 and 47")
    # plt.ylabel("Chi 1 of Histidine 334")
    # plt.legend(loc="upper right")
    # # plt.show()
    # plt.savefig('RhAG_di2_loop2_pH'+str(n+1) + '.png', bbox_inches='tight')
    # plt.close()
#
#
# for n in range(0,10,1):
#     hisAng = np.loadtxt(filenameB2(n))
#     xarray = hisAng[:, 0]
#     yarray = hisAng[:, 1]
#     plt.scatter(xarray, yarray)
#     plt.title("Histidine Dihedral vs Frame for RhBG at pH"+str(n+1))
#     plt.xlabel("Frame")
#     plt.ylabel("Dihedral of Histidine 186")
#     plt.legend(loc="upper right")
#     # plt.show()
#     plt.savefig('RhBG_di_his186_pH'+str(n+1) + '.png', bbox_inches='tight')
#     plt.close()
#     hisAng = np.loadtxt(filenameB3(n))
#     xarray = hisAng[:, 0]
#     yarray = hisAng[:, 1]
#     plt.scatter(xarray, yarray)
#     plt.title("Histidine Dihedral vs Frame for RhBG at pH"+str(n+1))
#     plt.xlabel("Frame")
#     plt.ylabel("Dihedral of Histidine 345")
#     plt.legend(loc="upper right")
#     # plt.show()
#     plt.savefig('RhBG_di_his345_pH'+str(n+1) + '.png', bbox_inches='tight')
#     plt.close()
#
# for n in range(0,10,1):
#     hisAng = np.loadtxt(filenameC2(n))
#     xarray = hisAng[:, 0]
#     yarray = hisAng[:, 1]
#     plt.scatter(xarray, yarray)
#     plt.title("Histidine Dihedral vs Frame for RhCG at pH"+str(n+1))
#     plt.xlabel("Frame")
#     plt.ylabel("Dihedral of Histidine 185")
#     plt.legend(loc="upper right")
#     # plt.show()
#     plt.savefig('RhCG_di_his185_pH'+str(n+1) + '.png', bbox_inches='tight')
#     plt.close()
#     hisAng = np.loadtxt(filenameC3(n))
#     xarray = hisAng[:, 0]
#     yarray = hisAng[:, 1]
#     plt.scatter(xarray, yarray)
#     plt.title("Histidine Dihedral vs Frame for RhCG at pH"+str(n+1))
#     plt.xlabel("Frame")
#     plt.ylabel("Dihedral of Histidine 344")
#     plt.legend(loc="upper right")
#     # plt.show()
#     plt.savefig('RhCG_di_his344_pH'+str(n+1) + '.png', bbox_inches='tight')
#     plt.close()