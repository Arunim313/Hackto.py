from pygame import mixer
from tkinter import *

root = Tk()
root.geometry("600x300")

mixer.init()
mixer.music.load("filename.mp3")


def pause():
    mixer.music.pause()


def play():
    mixer.music.play()


def resume():
    mixer.music.unpause()


Label(root, text="Welcome to music player", font="lucidia 30 bold").pack()
Button(text="Play", command=play).place(x=200, y=100)
Button(text="Pause", command=pause).place(x=250, y=100)
Button(text="Resume", command=resume).place(x=310, y=100)
Button(text="Quit", command=quit).place(x=380, y=100)

root.mainloop()