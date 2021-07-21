import numpy
import matplotlib.pyplot as plt

#USER SETTINGS
#Relative Path to Test Dataset = "Resources/syn_hcstLm.npy"
_path = "Resources/syn_hcstLm.npy"
dayIndex = 0

myEnsembleData = numpy.load(_path)
print("successfully loaded the data into memory.")

plt.plot(myEnsembleData[dayIndex])
plt.show()