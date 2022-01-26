import os
import shutil
import time

def RemoveFiles():
    deletedFolderCount = 0
    deletedFileCount = 0

    path = "/file1.txt"
    
    days = 0

    seconds = time.time() - (days*24*60*60)


    if os.path.exists(path):

        for rootFolder , folders, files in os.walk(path):

            if seconds >= getFileOrFolderAge(rootFolder):
                removeFolder(rootFolder)
                deletedFolderCount += 1
                break

            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolder , folder )    

                    if seconds >= getFileOrFolderAge(folderPath):
                        removeFolder(folderPath)
                        deletedFolderCount += 1

                for file in files:
                    filePath = os.path.join(rootFolder , file )    

                    if seconds >= getFileOrFolderAge(filePath):
                        removeFile(filePath)
                        deletedFileCount += 1

        else:
            if seconds >= getFileOrFolderAge(path):
                removeFile(file)
                deletedFileCount += 1
            
    else:
        print("Path not found!! ")


    print("Total Files deleted --> " , deletedFileCount)
    print("Total Folders deleted --> " , deletedFolderCount)



def removeFolder(path):
    if not shutil.rmtree(path):
        print("folder has been Deleted")
    else:
        print("Unable to delete! ")


def removeFile(path):
    if not shutil.remove(path):
        print("file has been Deleted")
    else:
        print("Unable to delete! ")




def getFileOrFolderAge(path):
    ctime = os.stat(path).st_ctime
    return ctime


RemoveFiles()