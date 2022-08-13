from tkinter import *
from tkinter import ttk
import tkinter as tk
from pynput import keyboard
import pyautogui
import pyperclip
import sys
import os
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk
from threading import Thread


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)



root = tk.Tk()
root.title("smart clipboard")
root.geometry('500x250')
root.resizable(False, False)
icon_path = resource_path('./assets/icon.ico')
root.iconbitmap(default=icon_path)


screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight() # Height of the screen
width = 600 # Width 
height = 300 # Height 
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
# root.eval('tk::PlaceWindow . center')


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
        inp = inp.removeprefix('\n')
        inp = inp.removesuffix('\n')
        list_strings.append(inp)
        print(list_strings)

    input_string.delete(0, "end")
    input_string.config(wrap=None)
    input_string.focus()



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




def paste():
    global list_strings
    if not list_strings:
        pyautogui.alert('Empty!')
        return

    pyautogui.alert('press CapsLock to use clipboard \npress Esc to terminate app')
    global running

    listener = keyboard.Listener(on_release=on_release)
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
        os._exit(1)

    if key == keyboard.Key.caps_lock:
            if j<len(list_strings):
                print("j is " +str( j )+ ", len is " + str(len(list_strings)))
                pyperclip.copy(list_strings[j])
                pyautogui.hotkey('ctrl', 'v')
                j +=1 
            if j<len(list_strings)-1:
                print(list_strings[j],"copied")
                  
            

add_strings_label = tk.Label( frame, text="Add you text here:")
add_strings_label.pack(padx=20, pady=5)


input_string = ttk.Entry(frame)
input_string.bind('<Return>', lambda x: add_string())
# input_string.bind('<Return>',  (lambda event: add_string()))
input_string.pack(fill='x',padx=20, pady=10)
input_string.focus()


add_button = ttk.Button(frame, text="add",command=add_string)
add_button.pack(padx=10, pady=5)



def quit_window(icon, item):
    icon.stop()
    root.destroy()
    os._exit(1)

def hide_window():
   root.withdraw()
   icon_path = resource_path('./assets/icon.ico')

# def show_window(icon, item):
#    icon.stop()
#    root.after(0,root.deiconify())

   image=Image.open(icon_path)
#    menu=(item('Quit', quit_window), item('Show', show_window))
   menu=(item('Quit', quit_window), item('Show my list', show_my_list))
   icon=pystray.Icon("name", image, "My System Tray Icon", menu)
   icon.run()




thread_hide_window =Thread(target = hide_window)
thread_paste = Thread(target = paste)

def start_service():
    global list_strings
    if not list_strings:
        pyautogui.alert('Empty!')
        return

    global thread_hide_window
    global thread_paste 
    thread_hide_window.start()
    thread_paste.start()


mainmenu = Menu(frame)
mainmenu.add_command(label = "Start", command= start_service)
mainmenu.add_command(label = "Show My List", command= show_my_list)
root.config(menu = mainmenu)



root.mainloop()
