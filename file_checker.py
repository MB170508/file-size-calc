import os, keyboard, time, string, sys
from elevate import elevate
from io import StringIO
import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo

def get_size(path = '.'):
    size_type = ""
    total_size = 0
    os.path.dirname(path)
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    if total_size >= 1000000000:
        total_size = total_size / 1000000000
        size_type = "gigabytes"
    elif total_size >= 1000000:
        total_size = total_size / 1000000
        size_type = "megabytes"
    elif total_size >= 1000:
        total_size = total_size / 1000
        size_type = "kilobytes"
    elif total_size >= 0:
        size_type = "bytes"
    round_total_size = round(total_size, 1)
    size = f'{round_total_size} {size_type}'
    return str(size)

root = tk.Tk()
root.title("Size calculation")

def browse():
    global path
    path = filedialog.askdirectory(parent=root,title='Select directory to detect subdir sizes')

user_path = str(os.path.expanduser( '~' ))

files = str( user_path.replace("\\", "/") + '/AppData/Local/Temp/files.txt')

def calculate():
    if os.path.exists(files):
            os.remove(files)
    path.replace("\\", "/")
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():
                wrt = str((entry.name) + " " + get_size(path + "/" + entry.name))
                with open(files, 'a') as f:
                    f.write(wrt)
                    f.write("\n")
                    f.close()
    showinfo(
    title='Information',
    message='   Done!  '
    )
    root.destroy()
    os.system(files + "\nQUIT")
    quit()

button = tk.Button(root, text='Browse Files', width=35, command=browse)
button2 = tk.Button(root, text='Calculate', width=35, command=calculate)

button.pack()
button2.pack()
root.mainloop()