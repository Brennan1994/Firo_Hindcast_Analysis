#Purpose: synthetic ensemble forecast data was provided in .npy format, as an 3D array. This script creates a csv file for each day, with all traces.
from msilib.schema import Directory
import numpy
import os 

#USER SETTINGS
#Relative Path to Test Dataset = "Resources/"
directory = "C:\\Users\\q0hecbbb\\Projects\\Hindcast_Revisited\\fromZach22June10"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        myEnsembleData = numpy.load(f,allow_pickle=True)
        print("successfully loaded the data into memory.")
        for eachLocation in myEnsembleData.files:
            DayNumFileName = 0
            for eachDay in myEnsembleData[eachLocation]:
                numpy.savetxt(directory +"\\AsCSV\\" + eachLocation + "\\" +  filename + eachLocation + str(DayNumFileName) + '.csv', eachDay, delimiter=',')
                DayNumFileName +=1
            print("finished " + eachLocation + " in " + filename)
print("successfully saved all the data to csv's.")

