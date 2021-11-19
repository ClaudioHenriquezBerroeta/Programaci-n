from tkinter import *
ventana = Tk()


def suma():
  ventanaSuma = Tk()
  ventanaSuma.title('Suma')
  ventanaSuma.geometry('400x200')

  def sumar():
    try:
      a=int(txtValor1.get())  #input
      b=int(txtValor2.get())  #input
      res=a+b
      txtResultado.config(state=NORMAL)
      txtResultado.delete(first=0,last=END)
      txtResultado.insert(0,res)  #print
      txtResultado.config(state='readonly')
    except:
      print('Error, celdas vacías o valores no son numéricos')

    
  def limpiar():
    txtValor1.delete(first=0,last=END)
    txtValor2.delete(first=0,last=END)
    txtResultado.config(state=NORMAL)
    txtResultado.delete(first=0,last=END)
    txtResultado.config(state='readonly')


  lblValor1 = Label(ventanaSuma, text='Valor 1')
  lblValor2 = Label(ventanaSuma, text='Valor 2')
  lblValor1.place(x= 70,y=20)
  lblValor2.place(x= 70,y=40)

  txtValor1 = Entry(ventanaSuma)
  txtValor1.place(x=140,y=20)
  txtValor2 = Entry(ventanaSuma)
  txtValor2.place(x=140,y=40)

  btnResultado=Button(ventanaSuma, text='Calcular',command=sumar).place(x=50,y=70)
  
  btnLimpiar = Button(ventanaSuma, text='Limpiar Valores', command=limpiar)
  btnLimpiar.place(x=160,y=70)

  txtResultado=Entry(ventanaSuma,state='readonly')
  txtResultado.place(x=150,y=120)


  lblResultado = Label(ventanaSuma, text='Resultado')
  lblResultado.place(x=20,y=120)
  
  btnSalir = Button(ventanaSuma,text='Salir',command=ventanaSuma.destroy)
  btnSalir.place(x=90, y=160)
  ventanaSuma.mainloop()
  

def resta():
  ventanaResta = Tk()
  ventanaResta.title('Resta')
  ventanaResta.geometry('400x200')


  def restar():
    try:
      a = int(txtValor1.get())
      b = int(txtValor2.get())
      res=a-b
      print(res)
      txtResultado.config(state=NORMAL)
      txtResultado.delete(first=0,last=END)
      txtResultado.insert(0,res)
      txtResultado.config(state='readonly')
    except:
      print('Error, celdas vacías o valores no son numéricos')

  def limpiar():
    txtValor1.delete(first=0,last=END)
    txtValor2.delete(first=0,last=END)
    txtResultado.config(state=NORMAL)
    txtResultado.delete(first=0,last=END)
    txtResultado.config(state='readonly')

  lblValor1 = Label(ventanaResta,text='Valor 1')
  lblValor1.place(x=10,y=30)
  txtValor1 = Entry(ventanaResta)
  txtValor1.place(x=100,y=30)

  lblValor2 = Label(ventanaResta,text='Valor 2')
  lblValor2.place(x=10,y=60)
  txtValor2 = Entry(ventanaResta)
  txtValor2.place(x=100,y=60)
  
  lblResultado = Label(ventanaResta,text='Resultado')
  lblResultado.place(x=10,y=90)
  txtResultado = Entry(ventanaResta, state='readonly')
  txtResultado.place(x=100,y=90)

  btnCalcular = Button(ventanaResta,text='Calcular',command=restar)
  btnCalcular.place(x=10,y=120)

  btnLimpiar = Button(ventanaResta,text='Limpiar',command=limpiar)
  btnLimpiar.place(x=200,y=120)

  btnSalir = Button(ventanaResta,text='Salir',command=ventanaResta.destroy)
  btnSalir.place(y=160, x='170')


def multiplicacion():
  ventanaMult = Tk()
  ventanaMult.title('Resta')
  ventanaMult.geometry('200x200')
  btnSalir = Button(ventanaMult,text='Salir',command=ventanaMult.destroy).place(y=160, x='70')

def division():
  ventanaDiv = Tk()
  ventanaDiv.title('Resta')
  ventanaDiv.geometry('200x200')
  btnSalir = Button(ventanaDiv,text='Salir',command=ventanaDiv.destroy).place(y=160, x='70')

ventana.title('Calculadora')
ventana.geometry('450x300')

posicion_y = 50
btnSuma=Button(ventana, text="Suma",command=suma).place(x=185,y=posicion_y+40*0)
btnResta=Button(ventana, text="Resta",command=resta).place(x=186,y=(posicion_y+40*1))
btnMult=Button(ventana, text="Multiplicación",command=multiplicacion).place(x=160,y=posicion_y+40*2)
btnDiv=Button(ventana, text="División",command=division).place(x=180,y=posicion_y+40*3)

btnSalir = Button(ventana,text='Salir',command=ventana.destroy).place(x=190, y=posicion_y+40*4)


ventana.mainloop()
