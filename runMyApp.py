import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables","*.exe"),("all files",".")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, fg= "white", bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

if os.path.isfile("saveApp.txt"):
    with open("saveApp.txt", 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

canvas = tk.Canvas(root, height =700, width =700, bg="white")
canvas.pack()

frame =tk.Frame(root, bg='grey')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white",bg ="#0067b8", command=addApp)
runApps = tk.Button(root, text="Run", padx=10, pady=5, fg="white",bg ="#0067b8",command=runApps)

openFile.pack()
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app, fg= "white", bg="gray")
    label.pack()

root.mainloop()

with open("saveApp.txt" , "w") as f:
    for app in apps:
        f.write(app + ",")