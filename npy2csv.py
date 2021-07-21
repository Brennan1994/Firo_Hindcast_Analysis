#Purpose: synthetic ensemble forecast data was provided in .npy format, as an 3D array. This script creates a csv file for each day, with all traces.
import numpy 

#USER SETTINGS
#Relative Path to Test Dataset = "Resources/syn_hcstLm.npy"
_path = "Resources/syn_hcstLm.npy"

myEnsembleData = numpy.load(_path)
print("successfully loaded the data into memory.")

DayNumFileName = 0 
for eachday in myEnsembleData:
    numpy.savetxt('Resources/syn_hcstLm' + str(DayNumFileName) + '.csv', eachday, delimiter=',')
    DayNumFileName +=1

print("successfully saved all the data to csv's.")

