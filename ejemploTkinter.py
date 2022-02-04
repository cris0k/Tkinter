from tkinter import *
from tkinter import ttk

class mainApp(Tk): # hereda de la clase Tk
    size = "640x480"
    
    def __init__(self):
        Tk.__init__(self) # constructor de la clase padre
        
        self.geometry(self.size)
        self.title("Mi ventana")
        self.configure(bg = "blue")
    
    def start(self):
        self.mainloop() # esto hace que empiece a funcionar y crea la ventana

if __name__ == '__main__':
    app = mainApp()
    app.start()

