import pylab

def filename(n):return '/home/blair/Documents/Mordor/RhAG_Cph/RhAG_watershell_'+str(n)+'.dat'
def label(n):return "pH = "+str(n+1)
list_of_files = [(filename(x),label(x)) for x in range(0,10,1)]

datalist = [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files ]

for data, label in datalist:
   pylab.plot( data[:,0], data[:,1], label=label)
   pylab.title("Number of Water within 3.4")
   pylab.xlabel("Frames")
   pylab.ylabel("Number")
   pylab.legend(loc="upper right")
   #pylab.show()
   pylab.savefig('watershell'+ label + '.png', bbox_inches='tight')
   pylab.close()