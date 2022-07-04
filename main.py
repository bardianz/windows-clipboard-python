from tkinter import *
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



frame = tk.Tk()
frame.title("smart clipboard")
frame.geometry('400x250')
frame.minsize(400,250)
# icon = resource_path('./assets/icon.ico')
# # icon = base64.b64decode(icon)
# # frame.iconbitmap()

# # frame.iconphoto(True, PhotoImage(data=icon))

# # frame.iconbitmap(resource_path('./assets/icon.ico'))


# ico = Image.open(icon)
# photo = ImageTk.PhotoImage(ico)
# frame.wm_iconphoto(False, photo)



list_strings=[]
i = 0
max = 0









def add_string():
    inp = input_string.get(1.0, "end-1c")
    if inp != '' and inp !='\n':
        print(inp + str(type(inp)))

        global list_strings
        print(list_strings)
        inp = inp.removeprefix('\n')
        inp = inp.removesuffix('\n')
        list_strings.append(inp)
        
        list_of_strings_lbl.config(text=list_strings)
    input_string.delete("1.0","end")
    input_string.config(wrap=None)


    

running = True

def start():
    frame.destroy()
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

# Button Creation


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
                  
            
            
                

# Label Creation
list_of_strings_lbl = tk.Label(frame, text="")
list_of_strings_lbl.pack(padx=20, pady=10)


add_strings_label = tk.Label( frame, text="add strings here:")
add_strings_label.pack(padx=20, pady=10)



input_string = tk.Text(frame, height=1, width=80,wrap=None)
input_string.bind('<Return>', lambda x: add_string())
# 
chxscrollbar=Scrollbar(input_string, orient=HORIZONTAL, command=input_string.xview)
input_string["xscrollcommand"]=chxscrollbar.set

# 

input_string.pack(padx=20, pady=10)

add_button = tk.Button(frame, text="add",command=add_string  )
add_button.pack(padx=10, pady=5)


start_button = tk.Button(frame, text="Start", command=start)
start_button.pack(padx=10, pady=5)

frame.mainloop()
