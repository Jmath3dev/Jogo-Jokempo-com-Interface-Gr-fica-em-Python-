import tkinter
from tkinter import *
from tkinter import ttk

# importando o pillow

from PIL import Image, ImageTk

import random


# cores -----------------------
co0 = "#FFFFFF" # white / branco
co1 = "#333333" # black / preto
co2 = "#fcc058" # orange / laranja
co3 = "#fff873" # yellow / amarelo
co4 = "#34eb3d" # green / verde
co5 = "#e85151" # red / vermelho
fundo = "#3b3b3b"

janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)


# dividindo a janela

frame_cima = Frame(janela, width= 260, height= 100, bg= co1, relief= 'raised')
frame_cima.grid(row= 0, column= 0, sticky = NW)

frame_baixo = Frame(janela, width= 260, height= 300, bg= co0, relief= 'flat')
frame_baixo.grid(row= 1, column= 0, sticky= NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')


# configurando o frame cima

app_1 = Label(frame_cima, text= "Você", height= 1, anchor= 'center', font=('Ivy 10 bold'), bg= co1, fg= co0)
app_1.place(x= 25, y=70)

app_1_linha = Label(frame_cima, text= "", height= 10, anchor= 'center', font=('Ivy 10 bold'), bg= co0, fg= co0)
app_1_linha.place(x= 0, y=0)

app_1_pontos = Label(frame_cima, text= "0", height= 1, anchor= 'center', font=('Ivy 30 bold'), bg= co1, fg= co0)
app_1_pontos.place(x= 50, y=20)


app_ = Label(frame_cima, text= ":", height= 1, anchor= 'center', font=('Ivy 30 bold'), bg= co1, fg= co0)
app_.place(x= 120, y=20)


app_2 = Label(frame_cima, text= "CPU", height= 1, anchor= 'center', font=('Ivy 10 bold'), bg= co1, fg= co0)
app_2.place(x= 205, y=70)

app_2_linha = Label(frame_cima, text= "", height= 10, anchor= 'center', font=('Ivy 10 bold'), bg= co0, fg= co0)
app_2_linha.place(x= 255, y=0)

app_2_pontos = Label(frame_cima, text= "0", height= 1, anchor= 'center', font=('Ivy 30 bold'), bg= co1, fg= co0)
app_2_pontos.place(x= 170, y=20)


app_linha = Label(frame_cima, text= "", width= 255, anchor= 'center', font=('Ivy 1 bold'), bg= co0, fg= co0)
app_linha.place(x= 0, y=95)

app_cpu = Label(frame_baixo, text= "", height= 1, anchor= 'center', font=('Ivy 10 bold'), bg= co0, fg= co0)
app_cpu.place(x= 190, y=10)

global voce
global cpu
global rounds
global pontos_voce
global pontos_cpu

pontos_voce = 0
pontos_cpu = 0
rounds = 5


# função lógica do jogo

# Função lógica do jogo
def jogar(i):
    global rounds, pontos_voce, pontos_cpu

    if rounds > 0:  # Verifica se ainda há rodadas disponíveis
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        cpu = random.choice(opcoes)
        voce = i

        app_cpu['text'] = cpu
        app_cpu['fg'] = co1

        # Verifica o resultado
        if voce == cpu:  # Empate
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3
        elif (voce == 'Pedra' and cpu == 'Tesoura') or (voce == 'Papel' and cpu == 'Pedra') or (voce == 'Tesoura' and cpu == 'Papel'):  # Vitória
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co5
            app_linha['bg'] = co0
            pontos_voce += 1
        else:  # Derrota
            app_1_linha['bg'] = co5
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0
            pontos_cpu += 1

        # Atualizar pontuação e rodadas
        app_1_pontos['text'] = str(pontos_voce)
        app_2_pontos['text'] = str(pontos_cpu)
        rounds -= 1
    else:
        fim_do_jogo()

# função iniciar o jogo

def iniciar_jogo(): 
   global icon_1, icon_2, icon_3
   global b_icon_1, b_icon_2, b_icon_3
  
   icon_1 = Image.open('images/pedra.png')
   icon_1 = icon_1.resize((50,50), Image.LANCZOS)
   icon_1 = ImageTk.PhotoImage(icon_1)
   b_icon_1 = Button(frame_baixo, command= lambda: jogar('Pedra') , width= 50, image= icon_1, compound= CENTER, bg= co0, fg= co0, font= ('Ivy 10 bold'), anchor= CENTER, relief= FLAT)
   b_icon_1.place(x= 15, y= 60)

   icon_2 = Image.open('images/papel.png')
   icon_2 = icon_2.resize((50,50), Image.LANCZOS)
   icon_2 = ImageTk.PhotoImage(icon_2)
   b_icon_2 = Button(frame_baixo, command= lambda: jogar('Papel') , width= 50, image= icon_2, compound= CENTER, bg= co0, fg= co0, font= ('Ivy 10 bold'), anchor= CENTER, relief= FLAT)
   b_icon_2.place(x= 95, y= 60)

   icon_3 = Image.open('images/tesoura.png')
   icon_3 = icon_3.resize((50,50), Image.LANCZOS)
   icon_3 = ImageTk.PhotoImage(icon_3)
   b_icon_3 = Button(frame_baixo, command= lambda: jogar('Tesoura') , width= 50, image= icon_3, compound= CENTER, bg= co0, fg= co0, font= ('Ivy 10 bold'), anchor= CENTER, relief= FLAT)
   b_icon_3.place(x= 170, y= 60)

# função terminar o jogo

def fim_do_jogo():
     print(f"Placar final: Você {pontos_voce} x {pontos_cpu} CPU")



b_jogar = Button(frame_baixo, command= iniciar_jogo, width= 30, text= 'JOGAR', bg= fundo, fg= co0, font= ('Ivy 10 bold'), anchor= CENTER, relief= RAISED, overrelief= RIDGE)
b_jogar.place(x= 5, y= 151)




janela.mainloop()