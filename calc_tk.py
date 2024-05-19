import tkinter as tk
from tkinter import *
root = Tk()


class validadores:
    def validate_entry11(self, text):
        if text == '': return True
         # Permitir números, sinal de negativo e alguns símbolos
        allowed_characters = set('0123456789-.')

        for char in text:
            if char not in allowed_characters:
                return False
            return True

        # Garantir que o sinal de negativo apareça apenas no início
        if text.count('-') > 1 or ('-' in text and text.index('-') != 0):
            return False
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 100000000000
     # função que ativa botoes numericos
    
     

class Application(validadores):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.botoes()
        self.validaEntradas()
        root.mainloop()

    

    def validaEntradas(self):
        self.vcmd11 = (self.root.register(self.validate_entry11), '%P')
 
        self.principal_entry = Entry(self.frame1, font=('Calibri Light', 40, 'bold'), validate= 'key', validatecommand= self.vcmd11)
        self.principal_entry.place(relx=0.01, rely=0.01, relheight=0.99, relwidth=0.99)
        self.principal_entry.configure(justify=('right'))

    def btnumeros(self, numero):
       
       pegaNumero = self.principal_entry.get()
       self.principal_entry.delete(0, END)
       self.principal_entry.insert(0, str(pegaNumero) + str(numero))
       return

    def LimpaCampo(self):
        self.principal_entry.delete(0,END)
         
   #------------------------------------OPERAÇÕES---------------------------------------#
    def soma(self):
        PegaNumero = self.principal_entry.get()
        global primeiroNumero
        global operacao
        operacao = 'soma'
        primeiroNumero = float(PegaNumero)
        self.principal_entry.delete(0, END)
        return
   #-------------------------------------------------------------------------------------#
    def subtracao(self):
        PegaNumero = self.principal_entry.get()
        global primeiroNumero
        global operacao
        operacao = 'subtração'
        primeiroNumero = float(PegaNumero)
        self.principal_entry.delete(0, END)
        return
    #-------------------------------------------------------------------------------------#
    def divisao(self):
        PegaNumero = self.principal_entry.get()
        global primeiroNumero
        global operacao
        operacao = 'divisão'
        primeiroNumero = float(PegaNumero)
        self.principal_entry.delete(0, END)
        return
    #-------------------------------------------------------------------------------------#
    def multiplicacao(self):
        PegaNumero = self.principal_entry.get()
        global primeiroNumero
        global operacao
        operacao = 'multiplicação'
        primeiroNumero = float(PegaNumero)
        self.principal_entry.delete(0, END)
        return
    #-------------------------------------------------------------------------------------#
    def potencia(self):
        PegaNumero = self.principal_entry.get()
        global primeiroNumero
        global operacao
        operacao = 'potência'
        primeiroNumero = float(PegaNumero)
        self.principal_entry.delete(0, END)
        return
    #-------------------------------------------------------------------------------------#
    def raiz(self):
        PegaNumero = self.principal_entry.get()
        global primeiroNumero
        global operacao
        operacao = 'raiz'
        primeiroNumero = float(PegaNumero)
        self.principal_entry.delete(0, END)
        return
    #----------------------------------------------------------------------------------------#
    def igual(self):
        PegaNumero = self.principal_entry.get()
        self.principal_entry.delete(0, END)
        if operacao == 'soma':
            self.principal_entry.insert(0, primeiroNumero + float(PegaNumero))
        elif operacao == 'subtração':
            self.principal_entry.insert(0, primeiroNumero - float(PegaNumero))
        elif operacao == 'multiplicação':        
            self.principal_entry.insert(0, primeiroNumero * float(PegaNumero))
        elif operacao == 'divisão':
            self.principal_entry.insert(0, primeiroNumero / float(PegaNumero))
        elif operacao == 'potência':
            self.principal_entry.insert(0, primeiroNumero ** float(PegaNumero))
        elif operacao == 'raiz':
            self.principal_entry.insert(0,primeiroNumero ** (1/2))
        return

    def tela(self):
        self.root.title('Calculadora em Construção...')
        self.root.configure(background= '#708090')
        self.root.geometry('300x500')
        self.root.resizable(True, True)
        self.root.maxsize(width= 900, height= 780)
        self.root.minsize(width=400, height=300)

    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bd= 4, bg= '#87CEFA', highlightbackground= '#708090',
                            highlightthickness = 6 )
        self.frame1.place(relx=0.1 , rely=0.1, relwidth=0.81, relheight=0.3) 



    def botoes(self):
        ###Criar botoes: Soma, Subtração, Divisao, Multiplicação, Apagar, Limpar, e calcular(Enter)
        self.bt_soma = Button(self.root, text='+', font= ('arial', 15, 'italic'), command=self.soma)
        self.bt_soma.place(relx=0.75, rely=0.70, relheight=0.11, relwidth=0.15)
        #------------------------------------------------------------------------#
        self.bt_sub = Button(self.root, text='-', font= ('arial', 15, 'italic'), command=self.subtracao)
        self.bt_sub.place(relx=0.75, rely=0.60, relheight=0.11, relwidth=0.15)
        #------------------------------------------------------------------------#
        self.bt_div = Button(self.root, text='÷', font= ('arial', 15, 'italic'), command=self.divisao)
        self.bt_div.place(relx=0.75, rely=0.50, relheight=0.11, relwidth=0.15)
        #------------------------------------------------------------------------#
        self.bt_mult = Button(self.root, text='×', font= ('arial', 15, 'italic'), command=self.multiplicacao)
        self.bt_mult.place(relx=0.75, rely=0.40, relheight=0.11, relwidth=0.15)
        #------------------------------------------------------------------------#
        self.bt_igual = Button(self.root, text='=', font= ('arial', 15, 'italic'), command=self.igual)
        self.bt_igual.place(relx=0.7, rely=0.81, relheight=0.1, relwidth=0.2)
        #------------------------------------------------------------------------#
        self.bt_apagar = Button(self.root, text='C', font= ('arial', 15, 'italic'), command=self.LimpaCampo)
        self.bt_apagar.place(relx=0.6, rely=0.40, relheight=0.11, relwidth=0.15)
        #------------------------------------------------------------------------#
        self.bt_elevar = Button(self.root, text='^', font= ('arial', 15, 'italic'), command=self.potencia)
        self.bt_elevar.place(relx=0.3, rely=0.40, relheight=0.11, relwidth=0.15)
        #------------------------------------------------------------------------#
        self.bt_elevar = Button(self.root, text='√', font= ('arial', 15, 'italic'), command=self.raiz)
        self.bt_elevar.place(relx=0.45, rely=0.40, relheight=0.11, relwidth=0.15)
        #------------------------------------------------------------------------#
        self.bt_elevar = Button(self.root, text='.', font= ('arial', 15, 'italic'), command=lambda : self.btnumeros('.'))
        self.bt_elevar.place(relx=0.30, rely=0.81, relheight=0.1, relwidth=0.15)

        #-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/#
        #botoes dos numeros
        self.bt1 = Button(self.root, text='1', font= ('arial', 15, 'italic'), command=lambda : self.btnumeros(1))
        self.bt1.place(relx=0.3, rely=0.71, relheight=0.1, relwidth=0.15)
        #------------------------------------------------------------------------#
        self.bt2 = Button(self.root, text='2', font= ('arial', 15, 'italic'), command=lambda : self.btnumeros(2))
        self.bt2.place(relx=0.45, rely=0.71, relheight=0.1, relwidth=0.15)
        #------------------------------------------------------------------------#
        self.bt3 = Button(self.root, text='3', font= ('arial', 15, 'italic'), command=lambda : self.btnumeros(3))
        self.bt3.place(relx=0.6, rely=0.71, relheight=0.1, relwidth=0.15)
        #------------------------------------------------------------------------#
        self.bt4 = Button(self.root, text='4', font= ('arial', 15, 'italic'), command=lambda : self.btnumeros(4))
        self.bt4.place(relx=0.3, rely=0.61, relheight=0.1, relwidth=0.15)
        #------------------------------------------------------------------------#
        self.bt5 = Button(self.root, text='5', font= ('arial', 15, 'italic'), command=lambda : self.btnumeros(5))
        self.bt5.place(relx=0.45, rely=0.61, relheight=0.1, relwidth=0.15)
        #------------------------------------------------------------------------#
        self.bt6 = Button(self.root, text='6', font= ('arial', 15, 'italic'), command=lambda : self.btnumeros(6))
        self.bt6.place(relx=0.6, rely=0.61, relheight=0.1, relwidth=0.15)
        #------------------------------------------------------------------------#
        self.bt7 = Button(self.root, text='7', font= ('arial', 15, 'italic'), command=lambda : self.btnumeros(7))
        self.bt7.place(relx=0.3, rely=0.51, relheight=0.1, relwidth=0.15)
        #------------------------------------------------------------------------#
        self.bt8 = Button(self.root, text='8', font= ('arial', 15, 'italic'), command=lambda : self.btnumeros(8))
        self.bt8.place(relx=0.45, rely=0.51, relheight=0.1, relwidth=0.15)
        #------------------------------------------------------------------------#
        self.bt9 = Button(self.root, text='9', font= ('arial', 15, 'italic'), command=lambda : self.btnumeros(9))
        self.bt9.place(relx=0.6, rely=0.51, relheight=0.1, relwidth=0.15)
        #------------------------------------------------------------------------#
        self.bt0 = Button(self.root, text='0', font= ('arial', 15, 'italic'), command=lambda : self.btnumeros(0))
        self.bt0.place(relx=0.45, rely=0.81, relheight=0.1, relwidth=0.25)
        #------------------------------------------------------------------------#
Application()