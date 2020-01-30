import numpy as np
import matplotlib.pyplot as plt
def filenameA(n,pro):return '/home/blair/Documents/Mordor/'+pro+'_Trimer/'+pro+'_watershell1_'+str(n)+'.dat'
def filenameB(n,pro):return '/home/blair/Documents/Mordor/'+pro+'_Trimer/'+pro+'_watershell2_'+str(n)+'.dat'
def filenameC(num,pro):return '/home/blair/Documents/Mordor/'+pro+'_Trimer/'+pro+'_watershell3_'+ str(num) +'.dat'
def test_file(num,pro):return '/home/blair/Documents/Mordor/'+pro+'_Trimer/'+pro+'_watershell3_'+ str(num) +'.dat'
def labelV(n):return "pH = "+str(n+1)

#Array with 3 Protein Names
Protein = ["RhAG", "RhBG", "RhCG"]
#Loop through Proteins
for name in Protein:
    test_list = [(test_file(x,name),labelV(x)) for x in range(0,10,1)]
    list_of_filesC = [(filenameC(x,name),labelV(x)) for x in range(0,10,1)]
    datalistC = [ (np.loadtxt(file), label) for file, label in list_of_filesC ]
    fig, ax = plt.subplots()
    arrayC_avg=[]
    arrayC_std=[]
    n=0
    for data, label in datalistC:
        avg = np.average(data[:,2])
        std = np.std(data[:,2])
        arrayC_avg.append(avg)
        arrayC_std.append(std)
        n= n+1


    list_of_filesA = [(filenameA(x,name),labelV(x)) for x in range(0,10,1)]
    datalistA = [ (np.loadtxt(fileA), labelA) for fileA, labelA in list_of_filesA ]
    arrayA_avg=[]
    arrayA_std=[]
    n=0
    for data, label in datalistA:
        avg = np.average(data[:,2])
        std = np.std(data[:,2])
        arrayA_avg.append(avg)
        arrayA_std.append(std)
        n= n+1



    list_of_filesB = [(filenameB(x,name),labelV(x)) for x in range(0,10,1)]
    datalistB = [ (np.loadtxt(fileB), labelB) for fileB, labelB in list_of_filesB]
    arrayB_avg=[]
    arrayB_std=[]
    n=0
    for data, label in datalistB:
        avg = np.average(data[:,2])
        std = np.std(data[:,2])
        arrayB_avg.append(avg)
        arrayB_std.append(std)
        n= n+1
    xlabel = [x for x in range(1,11,1)]

    plt.errorbar(xlabel,arrayA_avg, yerr=arrayA_std, fmt='o', color="r", label="Monomer 1")
    plt.errorbar(xlabel, arrayB_avg, yerr=arrayB_std, fmt='o', color="b", label="Monomer 2")
    plt.errorbar(xlabel,arrayC_avg, yerr=arrayC_std, fmt='o', color="g", label="Monomer 3")

    plt.title("Number of Water within 5.0")
    plt.xlabel("pH")
    plt.ylabel("Number")
    plt.legend(loc="upper right", numpoints=1)
    plt.xlim([0,11])
    #plt.show()
    plt.savefig('/home/blair/Documents/temp/Watershell_avg_trimer_'+name+'.png', bbox_inches='tight')
