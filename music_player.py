import time
from tkinter import *
from tkinter import filedialog      
from pygame import mixer
import os

root=Tk()
root.title("Pranay's Music player")
root.geometry("485x700+590+10")
root.configure(background="#333333")
root.resizable(False,False)
mixer.init()


def AddMusic():
    path = filedialog.askdirectory()
    if path:
       os.chdir(path)
       songs = os.listdir(path)

       for song in songs:
              if song.endswith(".mp3"):
                     Playlist.insert(END, song)

def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


lower_frame=Frame(root,bg="#FFFFFF",width=485,height=180)
lower_frame.place(x=0,y=400)

image_icon=PhotoImage(file="logo png.png")
root.iconphoto(False,image_icon)

frameCnt = 5
frames = [PhotoImage(file='proj.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)
label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)



Menu=PhotoImage(file="menu.png")
Label(root,image=Menu).place(x=0,y=580,width=485,height=100)

Frame_music=Frame(root,bd=2,relief=RIDGE)
Frame_music.place(x=0,y=585,width=485,height=100)

Buttonplay=PhotoImage(file="play1.png")
Button(root,image=Buttonplay,bg="#FFFFFF",bd=0,height=60,width=60,command=PlayMusic).place(x=215,y=487)

Buttonstop=PhotoImage(file="stop1.png")
Button(root,image=Buttonstop,bg="#FFFFFF",bd=0,height=60,width=60,command=mixer.music.stop).place(x=130,y=487)

Buttonpause=PhotoImage(file="pause1.png")
Button(root,image=Buttonpause,bg="#FFFFFF",bd=0,height=60,width=60,command=mixer.music.pause).place(x=300,y=487)

Buttonvolume = PhotoImage(file="volume.png")
Button(root, image=Buttonvolume, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.unpause).place(x=20, y=487)

Volume1=PhotoImage(file="volume.png")
pane1=Label(root,image=Volume1).place(x=20,y=487)
Button(root,text="Browse Music",width=59,height=1,font=("calibri",12,"bold"),fg="black",bg="#FFFFFF",command=AddMusic).place(x=0,y=550)

Scroll=Scrollbar(Frame_music)
Playlist=Listbox(Frame_music,width=100,font=("Times new roman",10),bg="#333333",fg="grey",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH) 



root=mainloop()



