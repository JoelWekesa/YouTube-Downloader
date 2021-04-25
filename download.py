from pytube import YouTube
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

Folder_Name = ""

def openLocation():
    global Folder_Name
    Folder_Name=filedialog.askdirectory()
    if (len(Folder_Name) > 1) :
        locationError.config(text=Folder_Name, fg="green")
    else:
        locationError.config(text="Please select a folder", fg="red")

def downloadVideo():
    choice = videoChoices.get()
    url = videoEntry.get()

    if (len(url) > 1 ):
        linkError.config(text="")
        yt = YouTube(url)

        if (choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()
        elif (choice == choices[1]):
            select = yt.streams.filter(progressive=True, file_extension="mp4").last()
        elif (choice == choices[2]):
            select = yt.streams.filter(only_audio=TRUE).first()
    else:
        linkError.config(text="Please input link", fg="blue")
    

    select.download(Folder_Name)
    linkError.config(text="Downlad Complete!")
    

# ? Step 1, define the window
window = Tk() 
font = ('jost', 14)

# ? Step 2, define the title
window.title("Joel's YouTube Downloader")
# ? Step 3 , define the height and width of the window respectively
window.geometry('500x800')
window.columnconfigure(0, weight=1) # ? This is to put all elements in a container
videoLabel = Label(window, text = 'Paste your youtube url here.', font = font) #? Here we created the label for the video entry box
videoLabel.pack( side = TOP, ipadx = 50, ipady = 6)
# videoLabel.grid() #? we just added the label to the grid.
videoEntryVar = StringVar() # ? We are expecting a string input fom a user. 
videoEntry = ttk.Entry(window, justify=LEFT, textvariable=videoEntryVar)
videoEntry.focus_force()
videoEntry.pack(side = TOP, ipadx = 100, ipady = 8)
linkError = Label(window, text="Input url", fg="blue", font=("Arial", 10))
linkError.pack(side =TOP, ipadx = 50, ipady = 6)
qualityLabel = Label(window, text="Select video quality", font = font)
qualityLabel.pack(side =TOP, ipadx = 50, ipady = 6)
choices = ["Best Quality", "Lowest Quality", "Only Audio"]
videoChoices = ttk.Combobox(window, values=choices)
videoChoices.pack(side = TOP, ipadx = 20, ipady =6)
saveLabel = Label(window, text="Select path to save file", font = font)
saveLabel.pack(side =TOP, ipadx = 50, ipady = 6)
saveEntry = ttk.Button(window, text="Choose path", command=openLocation)
saveEntry.pack(side = TOP, ipadx = 20, ipady =6)
locationError = Label(window, text="Select a location to save your file", fg="blue", font=("Arial", 10))
locationError.pack(side =TOP, ipadx = 50, ipady = 6)
saveButton = ttk.Button(window, text="Save File", command=downloadVideo)
saveButton.pack(side = TOP, ipadx = 20, ipady =6)

window.mainloop()

# ? After creating the set up file, run python setup.py build to build the project.

