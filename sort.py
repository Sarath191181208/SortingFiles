from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import time
import os
import json

FileTypesDic = json.load(open('FileTypes.json'))

folder_to_track = "C:/Users/Vangipuram/Downloads"
folder_destination = "C:/Users/Vangipuram/Documents"

# creates a denstiny folder and


def TypeOf(name: str) -> str:
    if os.path.isdir(folder_to_track+"/"+name):
        TYPE = "FOLDER"
    else:
        TYPE = name
        TYPE = TYPE.upper()
        TYPE = TYPE.split(".")[1]

    if TYPE in FileTypesDic:
        FolderPath = FileTypesDic[TYPE]
        FolderPathSplit = FolderPath
        FolderPathSplit = FolderPathSplit.split("/")
        pre = ""
        for i in FolderPathSplit:
            if not os.path.exists(folder_destination+"/" + pre + i):
                os.mkdir(folder_destination+"/" + pre + i)
            pre += i + "/"
        name = check_name(FolderPath, name)
        return(FolderPath+"/"+name)
    else:
        if not os.path.exists(folder_destination+"/" + "unknown"):
            os.mkdir(folder_destination+"/" + "unknown")
        check_name("unknown", name)
        return ("unknown/"+name)

# checks for a name collison


def check_name(dir: str, name: str) -> str:
    i = 1
    while os.path.exists(folder_destination + "/" + dir + "/" + name):
        name = name.split(".")
        if i > 1:
            name[0] = name[0][:-1]
        name[0] += str(i)
        i += 1
        name = ".".join(name)
    return(name)


for filename in os.listdir(folder_to_track):
    src = folder_to_track+"/"+filename
    # Type of checks type of file and sorts into a folder of a category
    new_destination = folder_destination+"/"+TypeOf(filename)
    os.rename(src, new_destination)


class Myhandler(FileSystemEventHandler):
    def dispatch(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track+"/"+filename
            # TypeOf func assigns dir based on type of file
            new_destination = folder_destination+"/"+TypeOf(filename)
            os.rename(src, new_destination)


event_handler = Myhandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)

observer.start()


try:
    while True:
        time.sleep(20)
except KeyboardInterrupt:
    observer.stop()
observer.join()
