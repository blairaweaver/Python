import numpy as np
import matplotlib.pyplot as plt
def filenameA():return '/home/blair/Documents/Mordor/RhCG_Cph/RhCG_hisn_0.dat'
def filenameB():return '/home/blair/Documents/Mordor/RhCG_Cph/RhCG_his_di_0.dat'
#def filenameC(n):return '/home/blair/Documents/Mordor/RhCG_Cph/RhCG_ensemble_'+str(n)+'.dat'
#def labelV(n):return "pH = "+str(n+1)
hisDis= np.loadtxt(filenameA())
hisDih= np.loadtxt(filenameB())
xarray=hisDis[:,0]
yarray=hisDis[:,1]
zarray=hisDih[:,1]
# print xarray
# print yarray
# print zarray
# X,Y=np.meshgrid(xarray,yarray)
# plt.figure()
# CS = plt.contour(X,Y ,zarray )
# plt.clabel(CS, inline=1, fontsize=10)
# plt.title('Simplest default with labels')
# plt.show()
fig, ax = plt.subplots()
plt.plot(xarray,yarray)
plt.show()
plt.plot(xarray,zarray)
plt.show()


#help(plt.contour)
# list_of_filesC = [(filenameC(x),labelV(x)) for x in range(0,10,1)]
# datalistC = [ (np.loadtxt(filenameC), labelC) for filenameC, labelC in list_of_filesC ]
# fig, ax = plt.subplots()
# arrayC_avg=[]
# arrayC_std=[]
# n=0
# for data, label in datalistC:
#     avg = np.average(data[:,1])
#     std = np.std(data[:,1])
#     arrayC_avg.append(avg)
#     arrayC_std.append(std)
#     n= n+1


# list_of_filesA = [(filenameA(x),labelV(x)) for x in range(0,10,1)]
# datalistA = [ (np.loadtxt(filenameA), labelA) for filenameA, labelA in list_of_filesA ]
# arrayA_avg=[]
# arrayA_std=[]
# n=0
# for data, label in datalistA:
#     avg = np.average(data[:,1])
#     std = np.std(data[:,1])
#     arrayA_avg.append(avg)
#     arrayA_std.append(std)
#     n= n+1



# list_of_filesB = [(filenameB(x),labelV(x)) for x in range(0,10,1)]
# datalistB = [ (np.loadtxt(filenameB), labelB) for filenameB, labelB in list_of_filesB]
# arrayB_avg=[]
# arrayB_std=[]
# n=0
# for data, label in datalistB:
#     avg = np.average(data[:,1])
#     std = np.std(data[:,1])
#     arrayB_avg.append(avg)
#     arrayB_std.append(std)
#     n= n+1
# xlabel = [x for x in range(1,11,1)]

# plt.errorbar(xlabel,arrayA_avg, yerr=arrayA_std, fmt='o', color="r", label="RhAG")
# plt.errorbar(xlabel, arrayB_avg, yerr=arrayB_std, fmt='o', color="b", label="RhBG")
# plt.errorbar(xlabel,arrayC_avg, yerr=arrayC_std, fmt='o', color="g", label="RhCG")
#
# plt.title("Histidine Distance")
# plt.xlabel("pH")
# plt.ylabel("Average Distance")
# plt.legend(loc="upper right", numpoints=1)
# plt.xlim([0,11])
# #plt.show()
# plt.savefig('His_dis_avg_all.png', bbox_inches='tight')
