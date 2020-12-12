from tkinter import *
import os

master = Tk()
master.title("SELMARapp")
canvas = Canvas(master, width=450, height=150)
canvas.pack()

def Open_pravne_osebe():
    os.system("pogodba_in_prevzemni_za_pravne_osebe.py")
def Open_fizicne_osebe():
    os.system("pogodba_in_prevzemni_za_fizicno_osebo.py")
def close_window():
    master.destroy()


button = Button(master, text="Naroči prevoz vozila", command=None)
button.pack()
button1 = Button(master, text="Naroči PDI", command=None)
button1.pack()
button2 = Button(master, text="Naroči homologacijo", command=None)
button2.pack()
button3 = Button(master, text="RVC", command=None)
button3.pack()
button4 = Button(master, text="Najemna pogodba za pravno osebo", command=Open_pravne_osebe)
button4.pack()
button5 = Button(master, text="Najemna pogodba za fizično osebo", command=Open_fizicne_osebe)
button5.pack()
button6 = Button(master, text="Izhod", command=close_window)
button6.pack()

my_image = PhotoImage(file="C:\\Users\\ikogovsek\\Desktop\\IGOR\\Python\\pythonProject\\SELMAR logo.gif")
canvas.create_image(0, 0, anchor=NW, image=my_image)
mainloop()

# todo ime datoteke za prevzemni zapisnik
# todo datum in uro kreiranja dokumenta shrani v excel
# todo popravi izpis vrste dokumenta
# todo naredi dodatno okno za potrditev pred zaključkom
# todo VIN mora biti 14 mestno število (preveri kako je pri Mazdi in Citroenu)
# todo zakleni inputbox ko enkrat klikne ok
# todo excel read only za vse ostale
# todo preveri možnost shranjevanja v PDF
# todo možnost dodajanja več avtomobilov
