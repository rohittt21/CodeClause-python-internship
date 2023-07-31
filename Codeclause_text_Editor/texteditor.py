

#Rohit Loharkar 
#Codeclause Internship Task - Text Editor in Python


from tkinter import *
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb

from PIL import Image, ImageTk
import os


root = tk.Tk()
root.title("Python - Text Editor")
root.geometry('800x500')
root.resizable(0,0)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#icon = ImageTk.PhotoImage(Image.open('Notepad.png'))
#root.iconphoto(False, icon)

root.update()


def open_file():
    file = fd.askopenfilename(defaultextension='.txt', filetypes = [('All Files', '*.*'),('Text Files', '*.txt')])

    if file != '':
        root.title(f"{os.path.basename(file)}")
        text_area.delete(1.0, END)
        with open(file, 'r') as file_:
            text_area.insert(1.0, file_.read())
            file_.close()
    else:
        file =None

def open_new_file():
    root.title('Python - Text Editor')
    text_area.delete(1.0, END)

def save_file():
    global text_area
    file = text_area.get(1.0, END)
    if file == '':
        file = None

    else:
        file = open(file, 'w')
        file.write(text_area.get(1.0, END))
        file.close()
    
    if file in None:
        file = fd.asksaveasfilename(initialfile = 'Untitled.txt', defaultextension='.txt',
                                  filetypes = [("Text File","*.txt*"),
                                               ("Word Document","*.docx*"),
                                                ('PDF',"*.pdf*")])
    else:
        file = open(file, 'w')
        file.write(text_area.get(1.0, END))
        file.close()
        root.title(f"{os.path.basename(file)} - Notepad")

def exit_application():
    root.destroy()

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def cut_text():
    text_area.event_generate("<<Cut>>")

def select_all():
    text_area.event_generate("<<Control-Keypress-A>>")

def delete_last_char():
    text_area.event_generate("<<KP_Delete>>")

def about_notepad():
    mb.showinfo("About Notepad", "This is just another Notepad, but this is better than all others")

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')
file_menu.add_command(label="New", command = open_new_file)
file_menu.add_command(label="Open File", command = open_file)
file_menu.add_command(label="Save as", command = save_file)
file_menu.add_separator()
file_menu.add_command(label="Close File", command = exit_application)

menu_bar.add_cascade(label="File", menu = file_menu)

edit_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')

edit_menu.add_command(label="Copy", command = copy_text)
edit_menu.add_command(label="Cut", command = cut_text)
edit_menu.add_command(label="Paste", command = paste_text)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command = select_all)
edit_menu.add_command(label="Delete", command = delete_last_char)

menu_bar.add_cascade(label='Edit', menu=edit_menu)

root.config(menu=menu_bar)

text_area = Text(root,font=('Times New Roman', 12))
text_area.grid(sticky=NSEW)

scroller= Scrollbar(text_area, orient= VERTICAL)
scroller.pack(side = RIGHT, fill = Y)

scroller.config(command = text_area.yview)
text_area.config(yscrollcommand=scroller.set)


root.mainloop()
