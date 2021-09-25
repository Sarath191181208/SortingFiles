from tkinter import Tk , Label, Frame , Entry , Button , messagebox , HORIZONTAL
from tkinter.ttk import Progressbar
from tkinter.filedialog import askdirectory
import time
import os
import json


def main():
	FileTypesDic = json.load(open('FileTypes.json'))


	def TypeOf(name: str,folder_to_track :str,folder_destination) -> str:
	    if os.path.isdir(folder_to_track+"/"+name):
	        TYPE = "FOLDER"
	    else:
	        TYPE = name
	        TYPE = TYPE.upper()
	        TYPE = TYPE.split(".")[-1]

	    if TYPE in FileTypesDic:
	        FolderPath = FileTypesDic[TYPE]
	        FolderPathSplit = FolderPath
	        FolderPathSplit = FolderPathSplit.split("/")

	        # this variable is used to track path and append new path to check
	        pre = ""
	        for i in FolderPathSplit:
	            if not os.path.exists(folder_destination+"/" + pre + i):
	                os.mkdir(folder_destination+"/" + pre + i)
	            pre += i + "/"

	        name = check_name_collision(FolderPath, name , folder_destination)
	        return(FolderPath+"/"+name)
	    else:
	        if not os.path.exists(folder_destination+"/" + "unknown"):
	            os.mkdir(folder_destination+"/" + "unknown")
	        name = check_name_collision("unknown", name,folder_destination)
	        return ("unknown/"+name)

	def check_name_collision(dir: str, name: str,folder_destination:str) -> str:
	    '''
	        return: a new name wich doesn't collide with the ones in the directory
	    '''
	    i = 1
	    while os.path.exists(folder_destination + "/" + dir + "/" + name):
	        name = name.split(".")
	        if i > 1:
	            # removes the last trailing character
	            name[0] = name[0][:-1]
	        name[0] += str(i)
	        i += 1
	        name = ".".join(name)
	    return(name)

	def transfer(folder_to_track,folder_destination):
	    if not (os.path.exists(folder_to_track) and os.path.exists(folder_destination)):
	        print("doesn't exists")
	        return False

	    items = len(os.listdir(folder_to_track))
	    if items == 0 :return -1

	    step = 100/items

	    for filename in os.listdir(folder_to_track):
	        src = folder_to_track+"/"+filename

	        # Type of checks type of file and sorts into a folder of a category
	        new_destination = folder_destination+"/"+TypeOf(filename,folder_to_track,folder_destination)
	        os.rename(src, new_destination)

	        progress_bar['value'] += step
	        root.update_idletasks()
	    return True

	def set_src_path(src_entry):
		win = Tk()
		win.withdraw()
		path = askdirectory(title = 'Source path')
		if path == '' or path is None:
			messagebox.showwarning("Warning","Invalid file path")
			return

		src_entry.delete(0,"end")
		src_entry.insert(0,path)

	def set_des_path(des_entry):
		win = Tk()
		win.withdraw()
		path = askdirectory(title = 'Source path')
		if path == '' or path is None:
			messagebox.showwarning("Warning","Invalid file path")
			return
		des_entry.delete(0,"end")
		des_entry.insert(0,path)

	def execute(file_src,file_des):
		reply = messagebox.askyesno("Are you sure?",f"Do you want to sort the files in {file_src.get()}")
		
		if not reply :
			return

		src = file_src.get()
		des = file_des.get()
		print(src,des)
		rtn = transfer(src,des)
		if rtn == True:
			messagebox.showinfo("Info","Operation Complete")
			progress_bar['value'] = 0
		elif rtn == -1:
			 messagebox.showerror("Error","Source directory is empty")
		else:
			messagebox.showerror("Error","File Path doesn't exist")
	
	src_path = 'C:/sarath/src'
	des_path = 'C:/sarath/des'
	root = Tk()

	file_src_container = Frame()

	file_src_text = Label(file_src_container,text = 'Source Folder :')
	file_src = Entry(file_src_container, width = 40, borderwidth = 5)
	file_src_btn = Button(root,text = 'Select Source Folder',command = lambda:set_src_path(file_src))
	file_src.insert(0, src_path)

	horizontal_sep = Label(root,text = '      ')
	horizontal_sep2 = Label(root,text = '      ')
	horizontal_sep3 = Label(root,text = '      ')
	horizontal_sep4 = Label(root,text = '      ')
	horizontal_sep5 = Label(root,text = '      ')

	file_des_container = Frame()
	file_des_text = Label(file_des_container,text = "Destination Folder :")
	file_des = Entry(file_des_container, width = 40, borderwidth = 5)
	file_des_btn = Button(root,text = 'Select Destination Folder',command = lambda:set_des_path(file_des))
	file_des.insert(0, des_path)

	horizontal_sep.pack()

	file_src_text.pack(side = 'left')
	file_src.pack()
	file_src_container.pack()
	horizontal_sep3.pack()
	file_src_btn.pack()

	horizontal_sep2.pack()

	file_des_text.pack(side = 'left')
	file_des.pack()
	file_des_container.pack()
	horizontal_sep4.pack()
	file_des_btn.pack()

	horizontal_sep5.pack()

	exec_btn = Button(root,text = 'Execute',command = lambda:execute(file_src,file_des))
	exec_btn.pack()

	progress_bar = Progressbar(root,orient = HORIZONTAL,length = 100 , mode = "determinate")
	progress_bar.pack()
	
	root.mainloop()

if __name__ == '__main__':
	main()