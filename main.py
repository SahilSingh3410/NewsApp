from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer
import os

mixer.init()

root = Tk()
root.geometry('700x220')
root.title('Music player')
root.resizable(0,0)

def songPlay(name : StringVar , list:Listbox,status:StringVar):
    name.set(list.get(ACTIVE))

    mixer.music.load(list.get(ACTIVE))
    mixer.music.play()
    status.set('Playing Song')

def songStop(status:StringVar):
    mixer.music.stop()
    status.set('Song Stopped')
def load(listbox):
    os.chdir(filedialog.askdirectory(title='open a songs directory'))

    tracks = os.listdir()

    for item in tracks:
        listbox.insert(END,item)

def songPause(status:StringVar):
    mixer.music.pause()
    status.set('Song Paused')

def songResume(status:StringVar):
    mixer.music.unpause()
    status.set('Song Resumed')

song_frame = LabelFrame(root, text='Current Song', bg='LightBlue', width=400, height=80)
song_frame.place(x=0, y=0)
button_frame = LabelFrame(root, text='Control Buttons', bg='Turquoise', width=400, height=120)
button_frame.place(y=80)
listbox_frame = LabelFrame(root, text='Playlist', bg='RoyalBlue')
listbox_frame.place(x=400, y=0, height=200, width=300)

current_song = StringVar(root, value='<Not selected>')
song_status = StringVar(root, value='<Not Available>')

# Playlist ListBox
playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='Gold')
scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)
playlist.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=playlist.yview)
playlist.pack(fill=BOTH, padx=5, pady=5)
# SongFrame Labels
Label(song_frame, text='CURRENTLY PLAYING:', bg='LightBlue', font=('Times', 10, 'bold')).place(x=5, y=20)
song_lbl = Label(song_frame, textvariable=current_song, bg='Goldenrod', font=("Times", 12), width=25)
song_lbl.place(x=150, y=20)
# Buttons in the main screen
pause_btn = Button(button_frame, text='Pause', bg='Aqua', font=("Georgia", 13), width=7,command=lambda: songPause(song_status))
pause_btn.place(x=15, y=10)
stop_btn = Button(button_frame, text='Stop', bg='Aqua', font=("Georgia", 13), width=7,
                  command=lambda: songStop(song_status))
stop_btn.place(x=105, y=10)
play_btn = Button(button_frame, text='Play', bg='Aqua', font=("Georgia", 13), width=7,
                  command=lambda: songPlay(current_song, playlist, song_status))
play_btn.place(x=195, y=10)
resume_btn = Button(button_frame, text='Resume', bg='Aqua', font=("Georgia", 13), width=7,
                    command=lambda: songResume(song_status))
resume_btn.place(x=285, y=10)
load_btn = Button(button_frame, text='Load Directory', bg='Aqua', font=("Georgia", 13), width=35,
                  command=lambda: load(playlist))
load_btn.place(x=10, y=55)


root.update()
root.mainloop()