#PageUP = CTRL + Shift + O (webcam)
#PageDown = CTRL + Shift + M (mic)
#'B' = CTRL + Shift + K (raise / lower hand)
#
#Left button = PagUP ------> Cam
#Right button = PagDown -------> Mic
#Up button = Raise / Lower hand
#Estimated operation distance: 10m


import tkinter as tk
import pygetwindow as pgw
import keyboard
import os
import sys
from PIL import ImageTk, Image
from tkinter import Canvas, NW

 

def resource_path(relative_path): #PyInstaller temp path
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def buttonController(): #toggle button
    global window_ID

    #toggle
    if enableBTN["text"] == "Ativar":
        enableBTN["text"] = "Desativar"
        enableBTN["background"] = "#C4314B"
        infoCanvas.pack_forget() #hide canva
        window_ID = window.after(1000, windowHandler) #schedule a function to run

        send_hotkeys()
        
    else:
        window.after_cancel(window_ID) #since its a scheduled call, it can be cancelled
        window_ID = None #empty the ID so scheduler can no longer run
        enableBTN["text"] = "Ativar"
        enableBTN["background"] = "#5B5FC7"
        infoCanvas.pack_forget() #hide canva

        keyboard.unhook_all() #undo all hotkeys association


def windowHandler(): #recursive function to keep the Teams window maximized and active to prevend hotkeys being sent to another application
    global window_ID

    try:
        teamsWindow = pgw.getWindowsWithTitle('Microsoft Teams')[0]
        teamsWindow.maximize()
        teamsWindow.activate()
    except:
        pass
    
    window_ID = window.after(5000, windowHandler) #5 seconds span


def send_hotkeys(): #remap, lock and send hotkeys
    
    #when key is pressed, it calls a function to release the key and send the hotkey. Supress is set to true, so it sends olny the hotkey

    def callback_PageUP(event):
        keyboard.release('PageUp')
        keyboard.send('ctrl+shift+o') #camera

    def callback_PageDown(event):
        keyboard.release('PageDown')
        keyboard.send('ctrl+shift+m') #mic
    
    def callback_b(event):
        keyboard.release('b')
        keyboard.send('ctrl+shift+k') #hand
    
    keyboard.on_press_key('PageUp', callback_PageUP, suppress=True) #camera
    keyboard.on_press_key('PageDown', callback_PageDown, suppress=True) #mic
    keyboard.on_press_key('b', callback_b, suppress=True) #hand


def showInfo(): #display the creator info
    if infoBTN["text"] == "e":
        infoCanvas.pack() #show canva
        infoBTN["text"] = "d"
    else: 
        infoBTN["text"] == "d"
        infoCanvas.pack_forget() #hide canva
        infoBTN["text"] = "e"





#Desgin
window = tk.Tk()
window.resizable(False, False)
window.title("Teams Remote")
window.iconbitmap(resource_path('./Assets/TeamsRemote_icon.ico'))


#remote picture
remotePIC = ImageTk.PhotoImage(file=resource_path("./Assets/remote_new.png"))
width, height = remotePIC.width(), remotePIC.height() #set the width and height according to the original file
canvas = Canvas(window, 
                bg="white", 
                width=width, 
                height=height, 
                highlightthickness=0)
canvas.pack()
canvas.create_image(0, 0, image=remotePIC, anchor=NW)


#info button to display credits
infoBTN_PIC = ImageTk.PhotoImage(file=resource_path("./Assets/infoPIC.png"))
infoBTN = tk.Button(window,
                    text="e",
                    width=10,
                    height=10,
                    image=infoBTN_PIC,
                    relief="solid",
                    borderwidth=0,
                    command=showInfo)
infoBTN.place(x=248, y=0)


#enable/ disable button
enableBTN = tk.Button(window,
                      width="10",
                      text="Ativar",
                      pady="30",
                      padx="82",
                      background="#5B5FC7",
                      foreground="white",
                      relief="solid",
                      borderwidth=0,
                      font=('Segoe UI', 12, "bold"),
                      command=buttonController)
enableBTN.pack()


#info canva
infoCanvas = Canvas(window, 
                    bg="#424242", 
                    width=268, 
                    height=60, 
                    highlightthickness=0)
githubPIC = ImageTk.PhotoImage(file=resource_path("./Assets/github_logo2.png"))
infoCanvas.create_text(131,15, 
                       fill="white", 
                       text="Coded with love by Anderson Lobo")
infoCanvas.create_image(75, 25, 
                        image=githubPIC, 
                        anchor=NW)
infoCanvas.create_text(141,37, 
                       fill="white", 
                       text="/anderson96x")
infoCanvas.pack_forget()


window.mainloop()