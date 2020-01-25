from tkinter import *
from playsound import playsound
from random import sample
from PIL import ImageTk
import PIL.Image
from AppKit import NSScreen
from tkinter import *
from tkinter import messagebox
import os
import back
#pengaturan layar UI
width = int(NSScreen.mainScreen().frame().size.width)
height = int(NSScreen.mainScreen().frame().size.height)

class Deck:
    def __init__(self, master):
		
        self.card = self.Card()
        self.n_card = 52

        self.deck_img = Label(master, text='')

        deckimg = PhotoImage(file = os.path.dirname(os.path.abspath('front1.py')) + '/PNG/purple_back.png')
        self.deck_img.configure(image = deckimg)
        self.deck_img.image = deckimg

        self.card1, self.card1_text = "", StringVar()
        self.card1_text.set(self.card1)
        self.card1_label = Label(master, textvariable=self.card1_text)

        self.card2, self.card2_text = "", StringVar()
        self.card2_text.set(self.card2)
        self.card2_label = Label(master, textvariable=self.card2_text)

        self.card3, self.card3_text = "", StringVar()
        self.card3_text.set(self.card3)
        self.card3_label = Label(master, textvariable=self.card3_text)

        self.card4, self.card4_text = "", StringVar()
        self.card4_text.set(self.card4)
        self.card4_label = Label(master, textvariable=self.card4_text)

        self.message, self.label_text = "", StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text, font=("Comic Sans MS",25))
        self.shuffle_button = Button(master, text="Shuffle", font=("Comic Sans MS",20), command=self.shuffle, padx=5, pady=5)
        self.pick_button = Button(master, text="  Pick  ",font=("Comic Sans MS",20),command=self.pick, padx=11, pady=5)
        self.reset_button = Button(master, text="Reset",font=("Comic Sans MS",20),command=self.reset, padx=14, pady=5)
        self.exite_button = Button(master, text=" Exit ",font=("Comic Sans MS",20),command=self.exite, padx=15, pady=5)
							
        self.cards = Label(master, text='')

        self.ans, self.ans_text = "", StringVar()
        self.ans_text.set(self.ans)
        self.ans_label = Label(master, textvariable=self.ans_text, font=("Comic Sans MS",20))

        self.score, self.score_text = "", StringVar()
        self.score_text.set(self.score)
        self.score_label = Label(master, textvariable=self.score_text, font=("Comic Sans MS",20))
		#konfigurasi lokasi button
        self.label.place(x=width/2.45, y=0)
        self.shuffle_button.place(x=50, y=250)
        self.pick_button.place(x=50, y=300)
        self.reset_button.place(x=50, y=350)
        self.exite_button.place(x=50, y=400)

        self.ans_label.place(x=200, y=255)
        self.score_label.place(x=200, y=305)
      
        self.cards.place(x=width/2-173, y=height/2-250)
        self.deck_img.place(x=width/2+250, y=height/2-132)
		#konfigurasi button untuk hovering mouse
        self.shuffle_button.bind("<Enter>", self.on_enter_shuffle)
        self.shuffle_button.bind("<Leave>", self.on_leave_shuffle)

        self.pick_button.bind("<Enter>", self.on_enter_pick)
        self.pick_button.bind("<Leave>", self.on_leave_pick)

        self.reset_button.bind("<Enter>", self.on_enter_reset)
        self.reset_button.bind("<Leave>", self.on_leave_reset)
        
        self.exite_button.bind("<Enter>", self.on_enter_exite)
        self.exite_button.bind("<Leave>", self.on_leave_exite)
	#Pengaturan me-reset kartu
    def reset(self):
        self.ans = ''
        self.score = ''
        self.ans_text.set(self.ans)
        self.score_text.set(self.score)
        deckimg = PhotoImage(file = os.path.dirname(os.path.abspath('front1.py')) + '/PNG/purple_back.png')
        self.deck_img.configure(image = deckimg)
        self.deck_img.image = deckimg
        self.cards.configure(image = '')
        self.card = self.Card()
        self.n_card = 52
        playsound ('Vista.mp3')
        self.message = "Reset!  %d card(s) left" % (self.n_card)
        self.label_text.set(self.message)
        self.card1_text.set('')
        self.card2_text.set('')
        self.card3_text.set('')
        self.card4_text.set('')
        self.pick_button.configure(state=NORMAL)
        self.shuffle_button.configure(state=NORMAL)

	#Pengaturan pengocokan kartu
    def shuffle(self):
        self.ans = ''
        self.score = ''
        self.ans_text.set(self.ans)
        self.score_text.set(self.score)
        self.cards.configure(image = '')
        playsound ('SoundShuffling.mp3')
        self.message = "Shuffle!  %d card(s) left" % (self.n_card)
        self.label_text.set(self.message)
        self.card = sample(self.card, self.n_card)
        if self.n_card == 0:
            self.shuffle_button.configure(state=DISABLED)
            self.deck_img.configure(image = '')
        
#pengaturan pengambilan kartu
    def pick(self):
        card = [self.card[self.n_card-1][1], self.card[self.n_card-2][1],
                self.card[self.n_card-3][1], self.card[self.n_card-4][1]]
        ans = back.greedy24(card)
        score = back.score(ans)
        for i in range(len(card)):
            if card[i] == 1: card[i] = "Ace"
            elif card[i] == 11: card[i] = "Jack"
            elif card[i] == 12: card[i] = "Queen"
            elif card[i] == 13: card[i] = "King"
            else: card[i] = str(card[i])
        img = []
        path = os.path.dirname(os.path.abspath('front1.py'))
        playsound ('tone.mp3')
        for i in range(len(card)):
            if card[i] == '10':
                img.append(path + '/PNG/%s%s.png' % (card[i], self.card[self.n_card-(i+1)][0][0]))
            else:
                img.append(path + '/PNG/%s%s.png' % (card[i][0], self.card[self.n_card-(i+1)][0][0]))
        self.card1_text.set(self.card1)
        self.card2_text.set(self.card2)
        self.card3_text.set(self.card3)
        self.card4_text.set(self.card4)
        cardimg = collage(346, 528, img)
        self.cards.configure(image = cardimg)
        self.cards.image = cardimg

        del self.card[self.n_card-4:]
        self.n_card -= 4
        self.message = "Pick!  %d card(s) left" % (self.n_card)
        self.label_text.set(self.message)
        self.ans = 'Solution: ' + ans + ' = ' + str(eval(ans))
        self.ans_text.set(self.ans)
        self.score = 'Score: '+ str(score)
        self.score_text.set(self.score)
        if self.n_card == 0:
            self.pick_button.configure(state=DISABLED)
            self.deck_img.configure(image = '')
	
#pengaturan kartu
    def Card(self):
        listCard = []
        listNum = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        listSym = ["Diamonds","Clubs","Hearts","Spades"]
        for i in range(len(listSym)):
            for j in range(len(listNum)):
                listCard.append([listSym[i], listNum[j]])
        return listCard
	#message popup saat akan exit
    def exite(self):
        MsgBox = messagebox.askokcancel('!!','Are you sure?',icon='warning')
        if MsgBox == False:
            messagebox.showinfo('Returning...','You will now return to the application')
        else:
            exit()
#pengaturan warna saat mouse hovering di atas button
    def on_enter_shuffle(self, event):
        self.shuffle_button.configure(highlightbackground='#6E97D8')

    def on_leave_shuffle(self, enter):
        self.shuffle_button.configure(highlightbackground='white')
        
    def on_enter_pick(self, event):
        self.pick_button.configure(highlightbackground='#6E97D8')
        
    def on_leave_pick(self, enter):
        self.pick_button.configure(highlightbackground='white')
        
    def on_enter_reset(self, event):
        self.reset_button.configure(highlightbackground='#C93434')

    def on_leave_reset(self, enter):
        self.reset_button.configure(highlightbackground='white')
    
    def on_enter_exite(self, event):
        self.exite_button.configure(highlightbackground='#C93434')

    def on_leave_exite(self, enter):
        self.exite_button.configure(highlightbackground='white')
		
def collage(w, h, l):
    c = 2
    r = 2
    nw = w//c
    nh = h//r
    size = nw, nh
    newim = PIL.Image.new('RGB', (w, h))
    img = []
    for p in l:
        im = PIL.Image.open(p)
        im.thumbnail(size)
        img.append(im)
    i = 0
    x = 0
    y = 0
    for col in range(c):
        for row in range(r):
            newim.paste(img[i], (x, y))
            i += 1
            y += nh
        x += nw
        y = 0
    newim.save('cards.png')
    a = PhotoImage(file = 'cards.png')
    return a

