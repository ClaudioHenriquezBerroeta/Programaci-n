from tkinter import *
ventana = Tk()

#import tkinter
#ventana = tkinter.Tk()

#import tkinter as tk
#ventana= tk.Tk()

def calculo():
  a=valor1.get()  #input
  b=valor2.get()  #input
  res=a+b
  resultado.set(res)  #print
  #resultado.set(valor1.get()+valor2.get())
  #set se usa para asignar un valor
  #get se usa para obtener un valor
  #resultado=valor1+valor2

  print('funciona')

def limpiar():
  valor1.set(0)
  valor2.set(0)
  resultado.set('')
  print('limpia')

ventana.title('Mi primera interfaz')
ventana.geometry('500x200')
etiqueta1 = Label(ventana, text='Bienvenido')
etiqueta2 = Label(ventana, text='Sistema de Sumas')
etiqueta1.pack()
etiqueta2.pack()
etiqueta1.place(x=215,y=0)
etiqueta2.place(x=190,y=20)
lblValor1 = Label(ventana, text='Valor 1')
lblValor2 = Label(ventana, text='Valor 2')

lblValor1.place(x= 170,y=60)
lblValor2.place(x= 170,y=80)

valor1=IntVar()
valor2=IntVar()
txtValor1 = Entry(ventana, textvariable=valor1)
txtValor1.place(x=240,y=60)
txtValor2 = Entry(ventana, textvariable=valor2)
txtValor2.place(x=240,y=80)

btnResultado=Button(ventana, text="Calcular suma",command=calculo).place(x=100,y=120)

lblResultado = Label(ventana, text='Resultado')
lblResultado.place(x=170,y=160)

resultado=StringVar()
txtResultado=Entry(ventana,textvariable=resultado).place(x=250,y=160)

btnLimpiar = Button(ventana, text='Limpiar Valores', command=limpiar)
btnLimpiar.place(x=250,y=120)

ventana.mainloop()
