from tkinter import *

#Estrutura da Janela
calculadora = Tk()
calculadora.title('Primeira Janela')
calculadora.geometry('475x500+500+100')
calculadora.resizable(width=False, height=False)
calculadora.config(bg ='#022a3b')

 #Funçao dos números

def btNumeros(numero):
    pegaNumero = campoNumeros.get()
    campoNumeros.delete(0, END)
    campoNumeros.insert(0, str(pegaNumero) + str(numero))
    return

def limpaCampo():
    campoNumeros.delete(0, END)
    return

def adiciona():
    global primeiro_numero
    global operacao_atual
    primeiro_numero = float(campoNumeros.get())
    operacao_atual = "+"
    campoNumeros.delete(0, END)
    
def subtrai():
    global primeiro_numero
    global operacao_atual
    primeiro_numero = float(campoNumeros.get())
    operacao_atual = "-"
    campoNumeros.delete(0, END)
    
def multiplicacao():
    primeiro_numero = float(campoNumeros.get())
    global operador
    operador = "*"
    limpaCampo()
    return

def divisao():
    primeiro_numero = float(campoNumeros.get())
    global operador
    operador = "/"
    limpaCampo()
    return

def calcula():
    segundo_numero = float(campoNumeros.get())
    campoNumeros.delete(0, END)
    if operacao_atual == "+":
        resultado = primeiro_numero + segundo_numero
    elif operacao_atual == "-":
        resultado = primeiro_numero - segundo_numero

#entry
campoNumeros = Entry(calculadora, width = 50)
campoNumeros.place(x = 100, y =25)

#botoes
Bt1 = Button(calculadora, text='1', relief=FLAT, width=10, height= 3, command = lambda : btNumeros(1))
Bt1.place(x=50, y=150)

Bt2 = Button(calculadora, text='2', relief=FLAT, width=10, height= 3, command = lambda : btNumeros(2))
Bt2.place(x=150, y=150)

Bt3 = Button(calculadora, text='3', relief=FLAT, width=10, height= 3, command = lambda : btNumeros(3))
Bt3.place(x=250, y=150)

Bt4 = Button(calculadora, text='4', relief=FLAT, width=10, height= 3, command = lambda : btNumeros(4))
Bt4.place(x=50, y=225)

Bt5 = Button(calculadora, text='5', relief=FLAT, width=10, height= 3, command = lambda : btNumeros(5))
Bt5.place(x=150, y=225)

Bt6 = Button(calculadora, text='6', relief=FLAT, width=10, height= 3, command = lambda : btNumeros(6))
Bt6.place(x=250, y=225)

Bt7 = Button(calculadora, text='7', relief=FLAT, width=10, height= 3, command = lambda : btNumeros(7))
Bt7.place(x=50, y=300)

Bt8 = Button(calculadora, text='8', relief=FLAT, width=10, height= 3, command = lambda : btNumeros(8))
Bt8.place(x=150, y=300)

Bt9 = Button(calculadora, text='9', relief=FLAT, width=10, height= 3, command = lambda : btNumeros(9))
Bt9.place(x=250, y=300)

Bt0 = Button(calculadora, text='0', relief=FLAT, width=10, height= 3, command = lambda : btNumeros(0))
Bt0.place(x=150, y=375)

BtVirgula = Button(calculadora, text=',', relief=FLAT, width=10, height= 3)
BtVirgula.place(x=50, y=375)

BtIgual = Button(calculadora, text='=', relief=FLAT, width=10, height= 3, command=calcula)
BtIgual.place(x=250, y=375)

BtDivisao = Button(calculadora, text='/', relief=FLAT, width=10, height= 3, command = divisao)
BtDivisao.place(x=350, y=150)

BtMultiplicacao = Button(calculadora, text='x', relief=FLAT, width=10, height= 3, command = multiplicacao)
BtMultiplicacao.place(x=350, y=225)

BtSoma = Button(calculadora, text='+', relief=FLAT, width=10, height= 3, command = adiciona)
BtSoma.place(x=350, y=300)

BtSubtracao = Button(calculadora, text='-', relief=FLAT, width=10, height= 3, command = subtrai)
BtSubtracao.place(x=350, y=375)

BtC = Button(calculadora, text='C', relief=FLAT, width=10, height= 3, command = limpaCampo)
BtC.place(x=50, y=75)

BtPorcentagem = Button(calculadora, text='%', relief=FLAT, width=10, height= 3)
BtPorcentagem.place(x=150, y=75)

BtPotencia = Button(calculadora, text='!', relief=FLAT, width=10, height= 3)
BtPotencia.place(x=250, y=75)

BtRaiz = Button(calculadora, text='^', relief=FLAT, width=10, height= 3)
BtRaiz.place(x=350, y=75)



feitoPor = Label(calculadora, text='Desenvolvido por Vinicius')
feitoPor.place(x=150, y=455)

calculadora.mainloop()

