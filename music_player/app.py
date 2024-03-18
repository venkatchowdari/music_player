# import all the required packages
from tkinter import *
from pygame import mixer
import os

# Creating interface or root window
root=Tk()
root.iconbitmap('applogo.png')

# To make the size of the window static
root.resizable(0,0)

# To Insert a title to the created root window
root.title('Music Player')

# Function to play the song
def play():
    currentsong=playlist.get(ACTIVE)
    mixer.music.load(currentsong)
    mixer.music.play()

# Function to pause the song which is currently playing
def pause():
    mixer.music.pause()


# Function to play the next song
def play_next():
    current_index = playlist.curselection()
    next_index = (current_index[0] + 1) % playlist.size()
    playlist.selection_clear(current_index)
    playlist.selection_set(next_index)
    playlist.activate(next_index)
    play()

# Function to play the previous song
def play_previous():
    current_index = playlist.curselection()
    previous_index = (current_index[0] - 1) % playlist.size()
    playlist.selection_clear(current_index)
    playlist.selection_set(previous_index)
    playlist.activate(previous_index)
    play()

#Create Player Control Buttons
back_btn_img = PhotoImage(file='backward_btn.png')
forward_btn_img = PhotoImage(file='forward_btn.png')
play_btn_img = PhotoImage(file='play_btn.png')
pause_btn_img = PhotoImage(file='pause_btn.png')
stop_btn_img = PhotoImage(file='stop_btn.png')

# Intilaizing the mixer module
mixer.init()

# Creating a listbox where the list of songs are going to be displayed
playlist = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), width=30)
playlist.grid(columnspan=4)

# Specifying the path from where the list of songs need to displayed on the root window
os.chdir = os.chdir(r"C:\Users\91800\OneDrive\Desktop\music_player\songs")
songs = os.listdir()
for s in songs:
    playlist.insert(END, s)

# Creating button which is used to control the play,pause,resume and stop the song
playbtn = Button(root, text="Play", command=play,bg='yellow',fg='blue',  image=play_btn_img)
playbtn.grid(row=1, column=1)

pausebtn = Button(root, text="Pause", command=pause,bg='yellow',fg='red', image=pause_btn_img)
pausebtn.grid(row=1, column=2)

# Creating buttons for Next and Previous
next_btn = Button(root, text="Next", command=play_next, bg='cyan', fg='black', image=forward_btn_img)
next_btn.grid(row=1, column=3)

previous_btn = Button(root, text="Previous", command=play_previous, bg='cyan', fg='black',  image=back_btn_img)
previous_btn.grid(row=1, column=0)


# To execute the output window
mainloop()
