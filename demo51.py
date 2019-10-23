import csv

sampleFile = open('data\\excel_data1.csv')

sampleReader = csv.reader(sampleFile)
sampleData = list(sampleReader)

sampleFile.close()
print(type(sampleData))
for i in sampleData:
    print(i)