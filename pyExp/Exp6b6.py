#Merging DataFrames
import pandas as myPan
data1 = {
"ID": [1, 2, 3, 4, 5],
"Name": ["Anisha", "Merin", "Ishika", "Falguni", "Vanshika"],
"Address": ["Matunga", "Andheri", "Dadar", "Thane", "Dombivli"],
"Age": [19, 18, 19, 20, 20]
}
data2 = {
"Address": ["Matunga", "Andheri", "Dadar", "Thane", "Dombivli"],
"Age": [19, 18, 19, 20, 20]
}
dataFrame1 = myPan.DataFrame(data1)
dataFrame2 = myPan.DataFrame(data2)
myResult = myPan.merge(dataFrame1, dataFrame2)
print(myResult)