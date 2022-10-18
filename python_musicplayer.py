from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import os

root = Tk()
root.title('Music player')
root.geometry("920x670+190+75")
root.configure(bg="#0f1a2b")
root.resizable(False, False)

mixer.init()


def Add_Music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)


def Play_Music():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


# icon
image_icon = PhotoImage(file="menu.png")
root.iconphoto(False, image_icon)

# Button
Button_Play = PhotoImage(file="play_button.png")
Button(root, image=Button_Play, bg="#0f1a2b", bd=0, command=Play_Music, height=150, width=150).place(x=200, y=250)

Button_Stop = PhotoImage(file="stop_button.png")
Button(root, image=Button_Stop, bg="#0f1a2b", bd=0, command=mixer.music.stop, height=150, width=150).place(x=30, y=500)

Button_Resume = PhotoImage(file="presume_button.png")
Button(root, image=Button_Resume, bg="#0f1a2b", bd=0, command=mixer.music.unpause, height=150, width=150).place(x=200,
                                                                                                                y=500)
Button_Pause = PhotoImage(file="pause_button.png")
Button(root, image=Button_Pause, bg="#0f1a2b", bd=0, command=mixer.music.pause, height=150, width=150).place(x=370,
                                                                                                             y=500)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=500, y=200, width=400, height=250)

Button(root, text="Add Music", width=15, height=2, font=("times new roman", 12, "bold"), fg="Black", bg="#21b3de",
       command=Add_Music).place(x=500, y=150)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey",
                   selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()
