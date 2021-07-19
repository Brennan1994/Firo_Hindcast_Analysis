import numpy 

#USER SETTINGS
#Relative Path to Test Dataset = "Resources/syn_hcstLm.npy"
_path = "Resources/syn_hcstLm.npy"

myEnsembleData = numpy.load(_path)
print("successfully loaded the data into memory")

#Commented out because this doesnt work for the 3D array.
#numpy.savetxt('Resources/syn_hcstLm.csv', myEnsembleData, delimiter=',')
#print("saved data as .csv")