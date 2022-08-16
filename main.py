from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("400x350")
root.title("Youtube downloader ")

def download():
    try:
        myVar.set("Downloading...")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video downloaded successfully")
    except Exception as e:
        myVar.set("Mistake")
        root.update()
        link.set("Enter correct link")

# created the Label widget to welcome user
Label(root, text="Welcome to youtube\nDownloader Application", font="Consolas 15 bold").pack()
myVar = StringVar()
myVar.set("Enter the link below")
Entry(root, textvariable=myVar, width=40).pack(pady=10)
link = StringVar()
# created the Entry widget to get the link
Entry(root, textvariable=link, width=40).pack(pady=10)
# created and called the download function to download video
Button(root, text="Download video", command=download).pack()
Button(root,text='Quit',command= root.destroy).pack()
root.mainloop()