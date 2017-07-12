oldFileName = input('input filename')

oldFile = open(oldFileName, 'r')

oldFileNameFirstindex = oldFileName.find('.')

oldFileNameSecond = oldFileName[oldFileNameFirstindex :]

newFileName = oldFileName[:oldFileNameFirstindex]+'[copy]'+oldFileNameSecond

print(newFileName)

newFile = open(newFileName, 'w')

for line in oldFile.readlines():
    newFile.write(line)

oldFile.close()
newFile.close()