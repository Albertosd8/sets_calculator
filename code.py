from tkinter import *
import random
mainprogram = Tk()

#variables globales
set1 = [0]
set2 = [0]

mainprogram.title("Calculadora de conjuntos")
mainprogram.geometry("1440x810")
mainprogram.config(bg="white")

#saving sets choosed and random
def SaveSetA():
    setAfirstfilter = EntryA.get()
    global set1
    set1 = list(setAfirstfilter.split(","))
    print(set1)


def SaveSetB():
    setBfirstfilter = EntryB.get()
    global set2
    set2 = list(setBfirstfilter.split(","))
    print(set2)


def SaveCarA():
    cardinalitya = RandomEntryA.get()
    number = int(cardinalitya)
    global set1
    list1 = [0] * number
    counter = 0
    for x in range(number):
        list1[counter] = (random.randint(1, 101))
        counter = counter + 1
    set1 = list1
    print(set1)


def SaveCarB():
    cardinalityb = RandomEntryB.get()
    number = int(cardinalityb)
    global set2
    list2 = [0] * number
    counter = 0
    for x in range(number):
        list2[counter] = (random.randint(1, 101))
        counter = counter + 1
    set2 = list2
    print(set2)


#options fuctions
def interseccion():
    inter = list(set(set1) & set(set2))
    result.set(inter)
    print(inter)


def union():
    union = list(set(set1+set2))
    result.set(union)
    print(union)

def diferenciaA():
    difA = list(set(set1)-set(set2))
    result.set(difA)
    print(difA)


def diferenciaB():
    difB = list(set(set2)-set(set1))
    result.set(difB)
    print(difB)


def diferenciaSimetrica():
    resultsimetrica = list((set(set1) - set(set2))) + list((set(set2)-set(set1)))
    result.set(resultsimetrica)
    print(resultsimetrica)


def complementoA():
    compleb = list(set(set2) - set(set1))
    result.set(compleb)
    print(compleb)


def complementoB():
    complea = list(set(set1) - set(set2))
    result.set(complea)
    print(complea)

def productoCartesiano1():
    list1 = list(map(str,set1))
    list2 = list(map(str, set2))
    list3 = []
    for i in list1:
        for x in list2:
            list3.append("(" + i + "," + x + ")")
    result.set(list3)
    print(list3)


def productoCartesiano2():
    list1 = list(map(str,set2))
    list2 = list(map(str, set1))
    list3 = []
    for i in list1:
        for x in list2:
            list3.append("(" + i + "," + x + ")")
    result.set(list3)
    print(list3)


def productoCartesiano3():
    list1 = list(map(str,set1))
    list2 = list(map(str, set1))
    list3 = []
    for i in list1:
        for x in list2:
            list3.append("(" + i + "," + x + ")")
    result.set(list3)
    print(list3)


def productoCartesiano4():
    list1 = list(map(str,set2))
    list2 = list(map(str, set2))
    list3 = []
    for i in list1:
        for x in list2:
            list3.append("(" + i + "," + x + ")")
    result.set(list3)
    print(list3)


def conjuntopotenciaA():
    set = [[]]
    for x in set1:
        for i in set:
            set = set + [list(i) + [x]]
    result.set(set)
    print(set)

def conjuntopotenciaB():
    power_set = [[]]
    for elem in set2:
        for sub_set in power_set:
            power_set = power_set + [list(sub_set) + [elem]]
    result.set(power_set)
    print(power_set)

def cardinalidadA():
    numberofcarA = len(list(dict.fromkeys(set1)))
    result.set(numberofcarA)
    print(numberofcarA)


def cardinalidadB():
    numberofcarB = len(list(dict.fromkeys(set2)))
    global result
    result.set(numberofcarB)
    print(numberofcarB)

result = StringVar()


#StartMenu
menu = Frame(mainprogram, width=1440, height=810)
menu.config(bg="white")
menu.pack()

#top layer, the blue one with the title
toppt0 = Label(menu, bg="#101820", width=6, height=4)
toppt1 = Label(menu, bg="#101820", width=45, height=4)
toppt2 = Label(menu, bg="#101820", width=5, height=4)
toppt3 = Label(menu, bg="#101820", width=45, height=4)
toppt4 = Label(menu, bg="#101820", width=5, height=4)
toppt5 = Label(menu, bg="#101820", width=45, height=4)
toppt6 = Label(menu, bg="#101820", width=6, height=4)
toppt0.grid(row=0, column=0)
toppt1.grid(row=0, column=1)
toppt2.grid(row=0, column=2)
toppt3.grid(row=0, column=3)
toppt4.grid(row=0, column=4)
toppt5.grid(row=0, column=5)
toppt6.grid(row=0, column=6)

title = Label(menu, text="Calculadora", fg="#D0D0CE", font=("Futura", 47), bg="#101820")
title.grid(row=0, column=1)
titlept2 = Label(menu, text="de", fg="#D0D0CE", font=("Futura", 47), bg="#101820")
titlept2.grid(row=0, column=3)
titlep3 = Label(menu, text="Conjuntos", fg="#D0D0CE", font=("Futura", 47), bg="#101820")
titlep3.grid(row=0, column=5)

#buttons
#Set A
bottomm = Label(menu)
bottomm.grid(row=1, column=3, pady=1)

SetA = Label(menu, text="Conjunto A", bg='#101820', foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
SetA.config(relief=FLAT)
SetA.grid(row=2, column=1)
EntryA = Entry(menu, bg="#F7F7F7", foreground='#101820', font=("Futura", 30), width=20, justify="center")
EntryA.grid(row=3, column=1)
ReadyA = Button(menu, command=lambda: SaveSetA(), text="Listo", bg="#F7F7F7", foreground="#383C4F", font=("Futura", 30), width=20, justify="center")
ReadyA.grid(row=5, column=1)

CarA = Label(menu, text="Cardinalidad para A", bg='#101820', foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
CarA.config(relief=FLAT)
CarA.grid(row=7, column=1)
RandomEntryA = Entry(menu, bg="#F7F7F7", foreground='#101820', font=("Futura", 30), width=20, justify="center")
RandomEntryA.grid(row=8, column=1)
MakeRandomA = Button(menu, command=lambda: SaveCarA(), text="Random", bg="#F7F7F7", foreground="#383C4F", font=("Futura", 30), width=20, justify="center")
MakeRandomA.grid(row=10, column=1)

Result = Label(menu, text="Resultado", bg='#101820', foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
Result.grid(row=13, column=1)
ResultBox = Label(menu, textvariable=result, bg="#F7F7F7", foreground='#101820', font=("Futura", 30), width=20, height=1)
ResultBox.grid(row=14, column=1)

#Set B

SetB = Label(menu, text="Conjunto B", bg='#101820', foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
SetB.config(relief=FLAT)
SetB.grid(row=2, column=3)
EntryB = Entry(menu, bg="#F7F7F7", foreground='#101820', font=("Futura", 30), width=20, justify="center")
EntryB.grid(row=3, column=3)
ReadyB = Button(menu, command=lambda: SaveSetB(), text="Listo", bg="#F7F7F7", foreground="#383C4F", font=("Futura", 30), width=20, justify="center")
ReadyB.grid(row=5, column=3)

CarB = Label(menu, text="Cardinalidad para B", bg='#101820', foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
CarB.config(relief=FLAT)
CarB.grid(row=7, column=3)
RandomEntryB = Entry(menu, bg="#F7F7F7", foreground='#101820', font=("Futura", 30), width=20, justify="center")
RandomEntryB.grid(row=8, column=3)
MakeRandomB = Button(menu, command=lambda: SaveCarB(), text="Random", bg="#F7F7F7", foreground="#383C4F", font=("Futura", 30), width=20, justify="center")
MakeRandomB.grid(row=10, column=3)


#Options for sets
#first 5
button1 = Button(menu, text="Intersección A ∩ B ",command=lambda: (interseccion()), bg="#383C4F", foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
button1.config(relief=FLAT)
button1.grid(row=2, column=5)
button2 = Button(menu, command=lambda: union(), text="Union  A u B", bg="#383C4F", foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
button2.config(relief=FLAT)
button2.grid(row=3, column=5)
button3 = Button(menu, command=lambda: diferenciaA(), text="Diferencia A -- B", bg="#383C4F", foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
button3.config(relief=FLAT)
button3.grid(row=4, column=5)
button4 = Button(menu, command=lambda: diferenciaB(), text="Diferencia B -- A", bg="#383C4F", foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
button4.config(relief=FLAT)
button4.grid(row=5, column=5)
button5 = Button(menu, command=lambda: diferenciaSimetrica(), text="Diferencia Simétrica A⊕B", bg="#383C4F", foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
button5.config(relief=FLAT)
button5.grid(row=6, column=5)

#second 5
button6 = Button(menu, command=lambda: complementoA(), text="Complemento A^c", bg="#383C4F", foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
button6.config(relief=FLAT)
button6.grid(row=7, column=5)
button7 = Button(menu, command=lambda: complementoB(), text="Complemento B^c", bg="#383C4F", foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
button7.config(relief=FLAT)
button7.grid(row=8, column=5)
button8 = Button(menu, command=lambda: productoCartesiano1(), text="Producto Cartesiano AxB", bg="#383C4F", foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
button8.config(relief=FLAT)
button8.grid(row=9, column=5)
button9 = Button(menu,  command=lambda: productoCartesiano2(), text="Producto Cartesiano BxA", bg="#383C4F", foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
button9.config(relief=FLAT)
button9.grid(row=10, column=5)
button10 = Button(menu, command=lambda: productoCartesiano3(), text="Producto Cartesiano AxA", bg="#383C4F", foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
button10.config(relief=FLAT)
button10.grid(row=11, column=5)

#third 5
button6 = Button(menu,  command=lambda: productoCartesiano4(), text="Producto Cartesiano BxB", bg="#383C4F", foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
button6.config(relief=FLAT)
button6.grid(row=12, column=5)
button7 = Button(menu, command=lambda: conjuntopotenciaA(), text="Conjunto Potencia (A)", bg="#383C4F", foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
button7.config(relief=FLAT)
button7.grid(row=13, column=5)
button8 = Button(menu, command=lambda: conjuntopotenciaB(), text="Conjunto Potencia (B)", bg="#383C4F", foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
button8.config(relief=FLAT)
button8.grid(row=14, column=5)
button9 = Button(menu, command=lambda: cardinalidadA(), text="Cardinalidad |A|", bg="#383C4F", foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
button9.config(relief=FLAT)
button9.grid(row=15, column=5)
button10 = Button(menu, command=lambda: cardinalidadB(), text="Cardinalidad |B|", bg="#383C4F", foreground="#D0D0CE", font=("Futura", 30), width=20, height=1)
button10.config(relief=FLAT)
button10.grid(row=16, column=5)


#bottom empty
bottom = Label(menu)
bottom.grid(row=17, column=3, pady=7)

mainprogram.mainloop()
