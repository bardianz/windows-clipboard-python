from tkinter import *
from tkinter import ttk
import tkinter as tk
from pynput import keyboard
import pyautogui
import pyperclip
import sys
import os
import base64
from PIL import Image, ImageTk



def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)



root = tk.Tk()
root.title("smart clipboard")
root.eval('tk::PlaceWindow . center')
root.geometry('500x250')
root.minsize(400,250)
icon_path = resource_path('./assets/icon.ico')
root.iconbitmap(default=icon_path)



frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill='x', expand=True)





list_strings=[]
i = 0
max = 0









def add_string():
    inp = input_string.get()
    if inp != '' and inp !='\n':
        print(inp + str(type(inp)))

        global list_strings
        print(list_strings)
        inp = inp.removeprefix('\n')
        inp = inp.removesuffix('\n')
        list_strings.append(inp)
        
    input_string.delete(0, "end")
    input_string.config(wrap=None)


def show_my_list():
    if not list_strings:
        pyautogui.alert('Empty!')
    else:
        string = ''
        for item in list_strings:
            string += item
            string += '\n'
        pyautogui.alert(string)
        

running = True

def start():
    root.destroy()
    pyautogui.alert('press CapsLock to use clipboard \npress Esc to terminate app')
    global list_strings
    global running

    print (list_strings)
    

    listener = keyboard.Listener(on_release=on_release)
    # run listener in background so that the while loop gets executed
    listener.start()

    while running:
        pass

    listener.stop()




j =0


def on_release(key):
    global running
    global list_strings
    global j
    if key == keyboard.Key.esc:
        running = False
        print('ended')
        pyautogui.alert('ended')
        sys.exit()

    if key == keyboard.Key.caps_lock:
            if j<len(list_strings):
                print("j is " +str( j )+ ", len is " + str(len(list_strings)))
                pyperclip.copy(list_strings[j])
                pyautogui.hotkey('ctrl', 'v')
                j +=1 
            if j<len(list_strings)-1:
                print(list_strings[j],"copied")
                  
            

add_strings_label = tk.Label( frame, text="add strings here:")
add_strings_label.pack(padx=20, pady=5)


input_string = ttk.Entry(frame)
input_string.bind('<Return>', lambda x: add_string())
# input_string.bind('<Return>',  (lambda event: add_string()))
input_string.pack(fill='x',padx=20, pady=10)
input_string.focus()


add_button = ttk.Button(frame, text="add",command=add_string)
add_button.pack(padx=10, pady=5)


# start_button = ttk.Button(frame, text="Start", command=start)
# start_button.pack(padx=10, pady=5)

mainmenu = Menu(frame)
mainmenu.add_command(label = "Start", command= start)
mainmenu.add_command(label = "Show My List", command= show_my_list)
root.config(menu = mainmenu)


frame.mainloop()
