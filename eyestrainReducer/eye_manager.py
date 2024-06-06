from tkinter import *
from tkinter.ttk import Progressbar
import time
from tkinter import messagebox
from playsound import playsound



app_info = """
The 20-20-20 rule can help prevent eye strain when looking at screens. For every 20 minutes a person looks at a screen, they should look at something 20 feet away for 20 seconds.

This app will pop up every 20 minutes, staying visible for 20 seconds before minimizing itself. Press the start button to begin."
"""


def wake_up():
    root.deiconify()
    root.attributes('-topmost', 1)
    bar()

def function_sound():
    playsound('tone.mp3', False)

def sleeping_for_20():
    root.attributes('-topmost', 0)
    root.withdraw() #totally hide window
    #root.iconify() #minimize the app 
    slp =1200000
    sleep_label = Label(root, text=f"Sleeping for {slp/60000} mins", font=("Courier", 14), bg="#26242f", fg="white")
    sleep_label.place(relx=0.5, rely=0.59, anchor='center')
    def sleep_fun():
        nonlocal slp
        if slp > 0:
            slp -= 1000
            sleep_label.config(text=f"Sleeping for {slp/60000} mins")  
            root.after(1000, sleep_fun) 
        else:
            sleep_label.destroy()
            wake_up()
    
    sleep_fun()
    


def more_info():
    messagebox.showinfo("More Info", app_info)


def start():
    
    root.after(1000, bar())
    


def bar():
    function_sound()
    progress_bar_value = 0 #progress bar value
    seconds = 0 #seconds to display
    
    progress = Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
    progress.place(relx=0.5, rely=0.7, anchor='center')

    look_label = Label(root, text="Please look at something 20 ft away for 20 seconds", font=("Courier", 14), bg="#26242f", fg="white")
    look_label.place(relx=0.5, rely=0.59, anchor='center')

    seconds_label = Label(root, text=seconds, font=("Courier", 25), bg="#26242f", fg="white")
    seconds_label.place(relx=0.5, rely=0.82, anchor='center')

    def update_progress():
        nonlocal progress_bar_value, seconds
        if progress_bar_value <= 100: #stop when progress bar gets done 
            seconds_label.config(text=f"{seconds}") #change displayed time
            progress['value'] = progress_bar_value # change progressbar value
            progress_bar_value += 5
            seconds += 1
            root.after(1000, update_progress)
        else:
            #destroying all created elements
            progress.destroy()
            look_label.destroy()
            seconds_label.destroy()
            sleeping_for_20()
    
    update_progress()


# create root window
root = Tk()  
root.geometry('600x300+700+300') #root window size and position
root.title("Eye strain manager")
root.config(bg="#26242f") #dark theam
p1 = PhotoImage(file='icon.png') #eye icon for title bar
root.iconphoto(False, p1)

#This btn will open up a dialog window to explain the app
more_inf_btn = Button(root, text='App info', command=lambda: more_info(), bd='5', activebackground='#646466', width = 10)
more_inf_btn.place(relx=1.0, rely=0.004, anchor='ne')


#This btn will start the progress
start_btn = Button(root, text='Start', command=lambda: start(), bd='5', activebackground='#646466', width = 10)
start_btn.place(relx=0.001, rely=0.11, anchor='sw')

root.mainloop()  # Tkinter event loop
