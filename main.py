from cgitb import text
from tkinter import *
import tkinter as tk
from pynput import keyboard
import pyautogui
import pyperclip
import sys

frame = tk.Tk()
frame.title("smart clipboard")
frame.geometry('400x250')

list_strings=[]
i = 0
max = 0









def add_string():
    inp = input_string.get(1.0, "end-1c")
    global list_strings
    list_strings.append(inp)
    list_of_strings_lbl.config(text=list_strings)
    input_string.delete("1.0","end")


    

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



input_string = tk.Text(frame, height=1, width=80)
input_string.pack(padx=20, pady=10)

add_button = tk.Button(frame, text="add",command=add_string  )
add_button.pack(padx=10, pady=5)


start_button = tk.Button(frame, text="Start", command=start)
start_button.pack(padx=10, pady=5)

frame.mainloop()
