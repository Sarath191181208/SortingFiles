# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler

import time
import os
import json
from FileManager import FileManager

if __name__ == '__main__':
    
    src = "C:/Users/Vangipuram/Downloads"
    des = "C:/Users/Vangipuram/Documents"
    file_manager = FileManager()
    file_manager.transfer(src,des)


    # class Myhandler(FileSystemEventHandler):
    #     def dispatch(self, event):
    #         for filename in os.listdir(folder_to_track):
    #             src = folder_to_track+"/"+filename
    #             # TypeOf func assigns dir based on type of file
    #             new_destination = folder_destination+"/"+TypeOf(filename)
    #             os.rename(src, new_destination)


    # event_handler = Myhandler()
    # observer = Observer()
    # observer.schedule(event_handler, folder_to_track, recursive=True)

    # observer.start()


    # try: 
    #     while True:
    #         time.sleep(20)
    # except KeyboardInterrupt:
    #     observer.stop()
    # observer.join()
