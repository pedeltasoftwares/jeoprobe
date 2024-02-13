import os
import tkinter as tk
from tkinter import filedialog

def list_files(directory):
    files = [file for file in os.listdir(directory) if file.endswith(".AT2")]
    return files

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        files = list_files(folder_path)
        file_listbox.delete(0, tk.END)
        for file in files:
            file_listbox.insert(tk.END, file)

def on_select():
    selected_files = [file_listbox.get(idx) for idx in file_listbox.curselection()]
    print("Archivos seleccionados:", selected_files)

root = tk.Tk()
root.title("Seleccionar Archivos .AT2")

select_folder_button = tk.Button(root, text="Seleccionar Carpeta", command=select_folder)
select_folder_button.pack(pady=10)

file_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=10)
file_listbox.pack(pady=10)

select_button = tk.Button(root, text="Seleccionar", command=on_select)
select_button.pack(pady=10)

root.mainloop()