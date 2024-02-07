
from tkinter import *
from tkinter import ttk

#importando Pillow
from PIL import Image, ImageTk

from dados import*

##cores##
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha


#criando Janela
Janela = Tk()
Janela.title ('Pokedex')
Janela.configure (background= co1)
Janela.geometry ('550x500')

ttk.Separator(Janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(Janela)
style.theme_use ("clam")

#criando frame
frame_pok = Frame (Janela, width=550, height=290, background=co0)
frame_pok.grid(row=1, column=0, padx=1, pady=1)

def troca_pokemon(i):
     global imagem_pokemon, imagem_pok

     #trocando a cor do fundo do frame
     frame_pok ['bg'] = pokemon [i] ['Tipo'][3]
#tipo de pokemon
     poke_nome['text'] = i
     poke_nome ['bg'] = pokemon[i]['Tipo'][3]
     poke_cat ['text'] = pokemon[i]['Tipo'][1]
     poke_cat ['bg'] = pokemon[i]['Tipo'][3]
     poke_id ['text'] = pokemon[i]['Tipo'][0]
     poke_id ['bg'] = pokemon[i]['Tipo'][3]

     imagem_pokemon = pokemon[i]['Tipo'][2]

     #imagens de fundo
     imagem_pokemon = Image.open(imagem_pokemon)
     imagem_pokemon = imagem_pokemon.resize ((230,230))
     imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

     imagem_pok = Label(frame_pok, image= imagem_pokemon, relief='flat', bg=pokemon[i]['Tipo'][3], fg=co1)
     imagem_pok.place (x=68,y=55)

     poke_nome.lift()

     #Status
     poke_hp ['text']= pokemon [i]['Status'][0]
     poke_ataque ['text']= pokemon [i]['Status'][1]
     poke_defesa ['text']= pokemon [i]['Status'][2]
     poke_velocidade['text'] = pokemon [i]['Status'][3]
     pokemon_total ['text']= pokemon [i]['Status'][4]

     #Habilidades
     poke_hb1 ['text'] = pokemon [i] ['Habilidades'] [0]
     poke_hb2 ['text'] = pokemon [i] ['Habilidades'] [1]

#nome
poke_nome = Label (frame_pok, text= '', relief="flat", anchor=CENTER, font=('fixedsys 20'), fg=co1)
poke_nome.place (x=12, y=15)

#categoria
poke_cat = Label (frame_pok, text= '', relief="flat", anchor=CENTER, font=('Ivy 10 bold'), fg=co1)
poke_cat.place (x=12, y=50)

#id
poke_id = Label (frame_pok, text= '', relief="flat", anchor=CENTER, font=('Ivy 10 bold'), fg=co1)
poke_id.place (x=12, y=75)


#status
poke_status = Label(Janela, text= 'Status', relief= 'flat', anchor=CENTER, font=('Verdadana 20'), bg=co1, fg=co0)
poke_status.place(x=15,y=310)

#HP
poke_hp = Label (Janela, text='HP:100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_hp.place (x=15,y=350)

#Ataque
poke_ataque = Label (Janela, text='Ataque:150', relief='flat', anchor=CENTER, font=('Verdana 10'),bg=co1, fg=co4)
poke_ataque.place (x=15, y=370)

#Defesa        
poke_defesa = Label (Janela, text='Defesa:100', relief='flat', anchor=CENTER,  font=('Verdana 10'), bg=co1, fg=co4)
poke_defesa.place (x=15, y=390)

#Velocidade
poke_velocidade = Label (Janela, text='Velocidade:100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_velocidade.place (x=15, y=410)

#Total
pokemon_total = Label(Janela, text='Total:100', anchor=CENTER, relief=  'flat', font=('Verdana 10'), bg=co1, fg=co4)
pokemon_total.place (x=15, y=430)

#Habilidades
poke_habilidades = Label (Janela, text='Habilidades', anchor=CENTER, relief='flat', font=('Verdana 20'), bg=co1, fg=co0)
poke_habilidades.place (x=180, y=310)

#Hab1
poke_hb1 = Label (Janela, text='Lança Chamas', anchor=CENTER, relief='flat', font=('Verdana 10'), bg=co1, fg=co4)
poke_hb1.place (x=195, y=350)

#Hab2
poke_hb2 = Label (Janela, text='Investida', anchor=CENTER, relief='flat', font=('Verdana 10'), bg=co1, fg=co4)
poke_hb2.place (x=195, y=370)

#Botões para pokemon1
imagem_painel_pokemon1 = Image.open ('Pokedex_img/images/cabeca-charmander.png')
imagem_painel_pokemon1 = imagem_painel_pokemon1.resize ((40,40))
imagem_painel_pokemon1 = ImageTk.PhotoImage(imagem_painel_pokemon1)

botao_poke1 = Button (Janela, command=lambda:troca_pokemon('Charmander'),image=imagem_painel_pokemon1, text='Charmander',width=150, relief='raised', overrelief=RIDGE, compound=LEFT, padx=5,  anchor=NW, font=('Verdana 12'), bg=co1, fg=co0 )
botao_poke1.place (x=370, y=10)

#Botões para pokemon2
imagem_painel_pokemon2 = Image.open ('Pokedex_img/images/cabeca-bulbasaur.png')
imagem_painel_pokemon2 = imagem_painel_pokemon2.resize ((40,40))
imagem_painel_pokemon2 = ImageTk.PhotoImage(imagem_painel_pokemon2)

botao_poke2 = Button (Janela, command=lambda:troca_pokemon('Bulbasaur'),image=imagem_painel_pokemon2, text='Bulbasaur',width=150, relief='raised', overrelief=RIDGE, compound=LEFT, padx=5,  anchor=NW, font=('Verdana 12'), bg=co1, fg=co0 )
botao_poke2.place (x=370, y=60)


#Botões para pokemon3
imagem_painel_pokemon3 = Image.open ('Pokedex_img/images/cabeca-gengar.png')
imagem_painel_pokemon3 = imagem_painel_pokemon3.resize ((40,40))
imagem_painel_pokemon3 = ImageTk.PhotoImage(imagem_painel_pokemon3)

botao_poke3 = Button (Janela, command=lambda:troca_pokemon('Gengar'),image=imagem_painel_pokemon3, text='Gengar',width=150, relief='raised', overrelief=RIDGE, compound=LEFT, padx=5,  anchor=NW, font=('Verdana 12'), bg=co1, fg=co0 )
botao_poke3.place (x=370, y=110)

#Botões para pokemon4
imagem_painel_pokemon4 = Image.open ('Pokedex_img/images/cabeca-pikachu.png')
imagem_painel_pokemon4 = imagem_painel_pokemon4.resize ((40,40))
imagem_painel_pokemon4 = ImageTk.PhotoImage(imagem_painel_pokemon4)

botao_poke4= Button (Janela, command=lambda:troca_pokemon('Pikachu'),image=imagem_painel_pokemon4, text='Pikachu',width=150, relief='raised', overrelief=RIDGE, compound=LEFT, padx=5,  anchor=NW, font=('Verdana 12'), bg=co1, fg=co0 )
botao_poke4.place (x=370, y=160)

#Botões para pokemon5
imagem_painel_pokemon5 = Image.open ('Pokedex_img/images/cabeca-gyarados.png')
imagem_painel_pokemon5 = imagem_painel_pokemon5.resize ((40,40))
imagem_painel_pokemon5 = ImageTk.PhotoImage(imagem_painel_pokemon5)

botao_poke5 = Button (Janela, command=lambda:troca_pokemon('Gyarados'),image=imagem_painel_pokemon5, text='Gyarados',width=150, relief='raised', overrelief=RIDGE, compound=LEFT, padx=5,  anchor=NW, font=('Verdana 12'), bg=co1, fg=co0 )
botao_poke5.place (x=370, y=210)

#Botões para pokemon6
imagem_painel_pokemon6 = Image.open ('Pokedex_img/images/cabeca-dragonite.png')
imagem_painel_pokemon6 = imagem_painel_pokemon6.resize ((40,40))
imagem_painel_pokemon6 = ImageTk.PhotoImage(imagem_painel_pokemon6)

botao_poke6 = Button (Janela, command=lambda:troca_pokemon('Dragonite'),image=imagem_painel_pokemon6, text='Dragonite',width=150, relief='raised', overrelief=RIDGE, compound=LEFT, padx=5,  anchor=NW, font=('Verdana 12'), bg=co1, fg=co0 )
botao_poke6.place (x=370, y=260)

Janela.mainloop ()