#Remap keys so you can use a simple presentation clicker to control the 'mute' and 'disable webcam' buttons on Teams application
#
#PageUP = CTRL + Shift + O (webcam)
#PAgeDown = CTRL + Shift + M (mic)
#According to the button order in Teams application
#
#Left button = PagUP ------> Cam
#Right button = PagDown -------> Mic
#Estimated operation distance: 10m


import tkinter as tk
import pygetwindow as pgw
import keyboard
import os
import sys
from PIL import ImageTk, Image
from tkinter import Canvas, NW

 
#PyInstaller temp path
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


#toggle button
def buttonController():
    global window_ID

    #toggle
    if enableBTN["text"] == "Ativar":
        enableBTN["text"] = "Desativar"
        enableBTN["background"] = "#C4314B"
        #window_ID = window.after(1000, windowHandler) #schedule a function to run

        #send_hotkeys()
        
    else:
        #window.after_cancel(window_ID) #since its a scheduled call, it can be cancelled
        #window_ID = None #empty the ID so scheduler can no longer run
        enableBTN["text"] = "Ativar"
        enableBTN["background"] = "#5B5FC7"

        #keyboard.unhook_all() #undo all hotkeys association


def windowHandler(): #recursive function to keep the Teams window maximized and active to prevend hotkeys being sent to another application
    global window_ID

    try:
        teamsWindow = pgw.getWindowsWithTitle('Microsoft Teams')[0]
        teamsWindow.maximize()
        teamsWindow.activate()
    except:
        pass
    
    window_ID = window.after(5000, windowHandler) #5 seconds span


def send_hotkeys():
    
    #when key is pressed, it calls a function to release the key and send the hotkey. Supress is set to true, so it sends olny the hotkey

    def callback_PageUP(event):
        keyboard.release('PageUp')
        keyboard.send('ctrl+shift+o') #camera

    def callback_PageDown(event):
        keyboard.release('PageDown')
        keyboard.send('ctrl+shift+m') #camera
    
    keyboard.on_press_key('PageUp', callback_PageUP, suppress=True) #camera
    keyboard.on_press_key('PageDown', callback_PageDown, suppress=True) #mic







#Desgin

window = tk.Tk()
window.resizable(False, False)
window.title("Teams Remote")
window.iconbitmap(resource_path('TeamsRemote_icon.ico'))


photoimage = ImageTk.PhotoImage(file=resource_path("remote.png"))
width, height = photoimage.width(), photoimage.height() #set the width and height according to the original file
canvas = Canvas(window, bg="white", width=width, height=height, highlightthickness=0)
canvas.pack()
canvas.create_image(0, 0, image=photoimage, anchor=NW)

enableBTN = tk.Button(window,
                      width="10",
                      text="Ativar",
                      pady="30",
                      padx="80",
                      background="#5B5FC7",
                      foreground="white",
                      relief="solid",
                      borderwidth=0,
                      font=('Segoe UI', 12, "bold"),
                      command=buttonController)
enableBTN.pack()




window.mainloop()