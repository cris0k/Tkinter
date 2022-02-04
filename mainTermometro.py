from tkinter import *
from tkinter import ttk

class mainApp(Tk): # hereda de la clase Tk
    entrada = None
    tipoUnidad = None
    size = "200x150"
    
    def __init__(self):
        Tk.__init__(self) # constructor de la clase padre
        
        self.geometry(self.size)
        self.title("Termómetro")
        self.configure(bg = "#ECECEC")
        self.resizable(0,0)
        
        self.temperatura = StringVar(value="") # StringVar es una variable de control que tiene una serie de atributos.
        self.trace("w", self.validateTemperature) # wru: write, read, unset. w: cada vez que se escfriba, va a llamar a la funcion indicada
        self.tipoUnidad = StringVar(value="C") # es un tipo de objeto que se le pueden asociar eventos
        
        self.createLayout()
        
    def createLayout(self):
        self.entrada = ttk.Entry(self, textvariable = self.temperatura).place(x=10, y=10) #este es la creacion del cuadrado de entry
        
        self.lblUnidad = ttk.Label(self, text= "Grados:").place(x=10, y=45)
        self.rb1 = ttk.Radiobutton(self, text="Fahrenheir", variable=self.tipoUnidad,value='F',command=self.selected).place(x=20, y=75)
        self.rb2 = ttk.Radiobutton(self, text="Celsius", variable=self.tipoUnidad,value='C',command=self.selected).place(x=20, y=105)
        
    def start(self):
        self.mainloop() # esto hace que empiece a funcionar y crea la ventana
    
    def validateTemperature(self,*args):
        nuevoValor = self.temperatura.get()
        print("nuevoValor", nuevoValor,"vs Valor Anterior", self.__temperaturaAnt)
        try:
            float(nuevoValor)
            self.temperaturaNat = nuevoValor
        except:
            self.temperatura.set(self.__temperaturaAnt)
    
    def selected(self):
        resultado = 0
        toUnidad = self.tipoUnidad.get()
        grados = float(self.temperatura.get())
        
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
            
        self.temperatura.set(resultado)



if __name__ == '__main__':
    app = mainApp()
    app.start()