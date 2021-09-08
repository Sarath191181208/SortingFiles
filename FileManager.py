import json
import os

class FileManager():
    def __init__(self):
        self.FileTypesDic = json.load(open('FileTypes.json'))

    def transfer(self,src_path,des_path ):

        for filename in os.listdir(src_path):

            if os.path.isdir(src_path +"/"+filename):
                continue

            file_path = src_path+"/"+filename
            # Type of checks type of file and sorts into a folder of a category
            new_destination = des_path +"/"+self.type_of(filename,src_path,des_path ) 
            os.rename(file_path, new_destination)

        return True

    def type_of(self,name: str,src_path :str,des_path : str) -> str:
        '''
            returns the new name of the the file and its respective folder
        '''
        
        if os.path.isdir(src_path +"/"+name):
            TYPE = "FOLDER"
        else:
            TYPE = name
            TYPE = TYPE.upper()
            TYPE = TYPE.split(".")[-1]

        if TYPE in self.FileTypesDic:
            FolderPath = self.FileTypesDic[TYPE]

            self.create_directory(FolderPath,des_path)
            name = self.check_name_collision(FolderPath, name , des_path)

            return(FolderPath+"/"+name)

        else:
            if not os.path.exists(des_path+"/" + "Unknown"):
                os.mkdir(des_path+"/" + "Unknown")

            name = self.check_name_collision("Unknown", name,des_path)
            return ("Unknown/"+name)

    def create_directory(self,FolderPath,des_path):

            FolderPathSplit = FolderPath
            FolderPathSplit = FolderPathSplit.split("/")

            # this variable is used to track path and append new path to check
            pre = ""
            for i in FolderPathSplit:

                if not os.path.exists(des_path +"/" + pre + i):
                    os.mkdir(des_path+"/" + pre + i)
                pre += i + "/"
    
    def check_name_collision(self,dir: str, name: str,folder_destination:str) -> str:
        '''
            return: a new name wich doesn't collide with the ones in the directory
        '''
        i = 1
        while os.path.exists(folder_destination + "/" + dir + "/" + name):
            name = name.split(".")
            if i > 1:
                # removes the last trailing character like 1,2,4....
                name[0] = name[0][:-1]
            name[0] += str(i)
            i += 1
            name = ".".join(name)
        return(name)

if __name__ == '__main__':
    manager = FileManager()
    # src = 'C:/sarath/src'
    # des = 'C:/sarath/des'
    # manager.transfer(src,des)
    print('done')
