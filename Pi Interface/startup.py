from tkinter import *
from time import *
from multiprocessing import *


class Timer:
    def time_loop(self, GUI):
        i=0
        start = time()
        time_out = start + 5
        
        while time() < time_out:
            if i == 4:
                self.GUI.lock_screen(master)
            print(i)
            i=i+1
            
        
        

class PrinterBotGUI:
    def __init__(self, master):
        self.master = master
        master.title("PrinterBot")
        master.iconbitmap(r'c:\Pi Interface\favicon.ico')
        master.geometry("700x400")

        welcome_lb = Label(master, font=("Helvetica", 25),text="[---Welcome To PrinterBot---]")
        welcome_lb.pack()
        welcome_lb.place(x=150, y=25)

        ent_btn = Button(master, text="[Enter]", command=lambda: self.start_up_handler(master),height = 10, width =25)
        ent_btn.pack()
        ent_btn.place(x=250, y=150)


    def lock_screen(self, master):
        self.clear_frame(master)
        self.master = master
        master.title("PrinterBot")
        master.iconbitmap(r'c:\Pi Interface\favicon.ico')
        master.geometry("700x400")

        welcome_lb = Label(master, font=("Helvetica", 25),text="[---Welcome To PrinterBot---]")
        welcome_lb.pack()
        welcome_lb.place(x=150, y=25)

        ent_btn = Button(master, text="[Enter]", command=lambda: self.start_up_handler(master),height = 10, width =25)
        ent_btn.pack()
        ent_btn.place(x=250, y=150)

    def start_up_handler(self,master):
        self.mainmenu(master)
             
    
    def clear_frame(self, master):
        for widget in master.winfo_children():
            widget.destroy()

    def mainmenu(self, master):
        self.clear_frame(master)

        cam_btn = Button(master, text="[----Cameras----]")
        cam_btn.pack()
        cam_btn.place(x=25, y=50)


        prnt_btn = Button(master, text="[----Printers----]")
        prnt_btn.pack()
        prnt_btn.place(x=25, y=100)

        stg_btn = Button(master, text="[----Settings----]")
        stg_btn.pack()
        stg_btn.place(x=25, y=150)

        qt_btn = Button(master, text="[----Quit----]", command=quit)
        qt_btn.pack()
        qt_btn.place(x=25, y=200)

        

root = Tk()
my_gui = Process(target=PrinterBotGUI(root))
my_timer = Process(target=Timer.time_loop(my_gui))
root.mainloop()
