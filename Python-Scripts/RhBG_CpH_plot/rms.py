import pylab

def filename(n):return '/home/blair/Documents/Mordor/RhBG_Cph/RhBG_rmsd_ca_'+str(n)+'.dat'
def label(n):return "pH = "+str(n+1)
list_of_files = [(filename(x),label(x)) for x in range(0,10,1)]

datalist = [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files ]

for data, label in datalist:
   pylab.plot( data[:,0], data[:,1], label=label)
   pylab.title("RMSD of RhBG")
   pylab.xlabel("Frames")
   pylab.ylabel("")
   pylab.legend(loc="upper right")
   #pylab.show()
   pylab.savefig(label + ' rmsd.png', bbox_inches='tight')
   pylab.close()