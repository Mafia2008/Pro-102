import os
import shutil

fromDir = 'C:/Users/zarif/Downloads/Coding/102/project'
toDir = 'C:/Users/zarif/Downloads/Coding/102/project/documents'

listOfFiles = os.listdir(fromDir)
print(listOfFiles)

for i  in listOfFiles:
    name,ext = os.path.splitext(i)
    if ext=='':
        continue
    if ext in ['.txt','.doc','.docx','.pdf']:
        path1 = fromDir+'/'+i
        path2 = toDir+'/'
        path3 = toDir+'/'+i

        if(os.path.exists(path2)):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
