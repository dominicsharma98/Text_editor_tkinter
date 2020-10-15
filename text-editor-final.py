from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile
import threading 
import time


def about():
	filewin = Toplevel(root)
	string = "This is a small text editor built during our Training\n"
	string += "This text editor unlike many others supports many functions like giving suggestions based on your previous data \n"
	string += "Small, easy to use and works like the future of text editors \n"
	button = Label(filewin,text=string)
	button.pack()
 
def open_file():
	global text,save_file_id
	open_file_loc=askopenfilename()
	open_file=open(open_file_loc,'r')
	text.delete(1.0,END)
	text.insert(END,open_file.read())
	save_file_id=open_file_loc

def save_as_file():
	global text,save_file_id,strn1
	strn1 = text.get(0.0,END)
	tempArr = strn1.split()
	makeCapital = True
	# makeSpace = False
	for index, word in enumerate(tempArr):
		for index1, char in enumerate(word):
			if(makeCapital):
				tempArr[index] = word[0].upper() + word[1:]
				makeCapital = False
			if(char in set([".", "?"]) and index1 != len(word) - 1):
				if(len(word) == 1):
					continue
				if(word[index1+1] != " "):
					# put Space
					if(index1 + 2 < len(word)):
						temp = word[0:index1+1] + " " + word[index1 +
																1:index1+2].upper() + word[index1+2:]
					else:
						temp = word[0:index1+1] + " " + \
							word[index1+1:index1+2].upper()
					tempArr[index] = temp
			if(char in set([".", "?"]) and index1 == len(word) - 1):
				makeCapital = True
			if(char in set([","]) and (index1 != len(word) - 1)):
				if(len(word) == 1):
					continue
				if(word[index1+1] != " "):
					temp = word[0:index1+1] + " " + word[index1+1:]
					tempArr[index] = temp

	strn1 = " ".join(tempArr)

	for index, char in enumerate(strn1):
		if(char in set([",", ".", "?"]) and strn1[index-1] == " " and strn1[index + 1] == " "):
			strn1 = strn1[:index-1] + char + strn1[index+1:]
	print(strn1)
	text.delete(0.0,END)
	text.insert(END,strn1)

	name=asksaveasfile(mode='w',defaultextension=".txt")
	text2save= strn1  
	name.write(text2save)
	name=str(name)[(str(name).find("name='")+6):str(name).find("'",(str(name).find("name='")+6))]
	save_file_id=name

def save_file():
	global text,save_file_id,strn1
	strn1 = text.get(0.0,END)
	tempArr = strn1.split()
	makeCapital = True
	# makeSpace = False
	for index, word in enumerate(tempArr):
		for index1, char in enumerate(word):
			if(makeCapital):
				tempArr[index] = word[0].upper() + word[1:]
				makeCapital = False
			if(char in set([".", "?"]) and index1 != len(word) - 1):
				if(len(word) == 1):
					continue
				if(word[index1+1] != " "):
					# put Space
					if(index1 + 2 < len(word)):
						temp = word[0:index1+1] + " " + word[index1 +
																1:index1+2].upper() + word[index1+2:]
					else:
						temp = word[0:index1+1] + " " + \
							word[index1+1:index1+2].upper()
					tempArr[index] = temp
			if(char in set([".", "?"]) and index1 == len(word) - 1):
				makeCapital = True
			if(char in set([","]) and (index1 != len(word) - 1)):
				if(len(word) == 1):
					continue
				if(word[index1+1] != " "):
					temp = word[0:index1+1] + " " + word[index1+1:]
					tempArr[index] = temp

	strn1 = " ".join(tempArr)

	for index, char in enumerate(strn1):
		if(char in set([",", ".", "?"]) and strn1[index-1] == " " and strn1[index + 1] == " "):
			strn1 = strn1[:index-1] + char + strn1[index+1:]
	print(strn1)

	if save_file_id=="":
		save_as_file()
	else:
		with open(save_file_id,'w') as f:
			f.write(strn1)
			text.delete(0.0,END)
			text.insert(END,strn1)


def New_file():
	text.delete(1.0, END)
	save_file_id = ' '


def undo():
	global undo_list,text
	text = undo_list.pop()


def drop_style(*args):
	txt = text.get(0.0,END)
	text.delete(0.0,END)
	text.configure(font = (var.get(), text_size))
	text.insert(0.0,txt)
	w.destroy()

def font_style():
	global text, var, w
	var = StringVar(root)
	var.set(text_style)
	match_list = ["Times New Roman", "Helvetica", "Ariel", "Courier","Symbol"]
	var.trace('w', drop_style)
	w = OptionMenu(root, var, *match_list)
	w.pack()

def drop_size(*args):
	txt = text.get(0.0,END)
	text.delete(0.0,END)
	text.configure(font = (text_style, var.get()))
	text.insert(0.0,txt)
	w.destroy()

def font_size():
	global var, w
	var = StringVar(root)
	var.set(text_size)
	match_list = [8, 10, 11, 12, 14]
	var.trace('w', drop_size)
	w = OptionMenu(root, var, *match_list)
	w.pack()

root = Tk()
root.title("jotter")

text=Text(root, width=200, undo=True)
text_size = 11
text_style = "Times New Roman"
text.configure(font=(text_style, text_size))
text.pack() 
save_file_id=""

menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label="New", command = New_file)
filemenu.add_command(label = "Open", command = open_file)
filemenu.add_command(label = "Save", command = save_file)
filemenu.add_command(label = "Save as...", command = save_as_file)
filemenu.add_command(label = "Exit", command = root.quit)    

Editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Edit", menu = Editmenu)
Editmenu.add_command(label = "Font Style", command = font_style)
Editmenu.add_command(label = "Font Size", command = font_size)


helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "About...", command = about)


root.config(menu = menubar)
root.mainloop()
