from tkinter import *
from tkinter import messagebox
import pygame

piano = Tk()
piano.title('피아니스트')
piano.geometry('350x300+0+0')
pygame.init()


def btn1_click():
    label = Label(piano, text='둘 중에 하나를 선택해주세요!' )
    label.pack()
    btn1 = Button( piano, width=8, height=5, text="피아노치기", bg="black", fg="white", command=pianist)
    btn1.pack()

    btn2 = Button(piano, width=8, height=5, text="게임하기", bg="black", fg="white" )
    btn2.pack()

    btn1.place( x=100, y=100 )
    btn2.place( x=200, y=100 )
    label.place( x=105, y=50 )


def btn2_click():
    btn2["text"] = "YES를 눌러"

label = Label(piano, text='피아니스트가 되어보실래요? ')
label.pack()
btn1=Button(piano, width=8, height=5, text="YES", bg="black", fg="white", command=btn1_click)
btn1.pack()

btn2=Button(piano, width=8, height=5, text="NO", bg="black", fg="white", command=btn2_click)
btn2.pack()
btn1.place(x=100, y=100)
btn2.place(x=200, y=100)
label.place(x=105, y=50)

def pianist():
    piano.title("Piano")
    piano.geometry('860x460+0+0')
    piano.configure(background='white')

    ABC = Frame(piano, bg="pink", bd=10, relief=RIDGE)
    ABC.grid()

    ABC1 = Frame(ABC, bg="pink", bd=5, relief=RIDGE)
    ABC1.grid()
    ABC2 = Frame(ABC, bg="pink", relief=RIDGE)
    ABC2.grid()
    ABC3 = Frame(ABC, bg="pink",relief=RIDGE)
    ABC3.grid()

    str1 = StringVar()
    str1.set("Piano")
# Date1 = StringVar()
# Time1= StringVar()
#
# Date1.set(time.strftime("%d/%m/%Y"))
# Time1.set(time.strftime("%H:%M:%S"))

    def value_Cs():
        str1.set("C#")
        sound=pygame.mixer.Sound("C:\music\Music_Notes\C_s.wav")
        sound.play()
        return


    def value_Ds():
        str1.set("D#")
        sound = pygame.mixer.Sound("C:\music\Music_Notes\D_s.wav")
        sound.play()
        return



    def value_Fs():
        str1.set("F#")
        sound = pygame.mixer.Sound("C:\music\Music_Notes\F_s.wav")
        sound.play()
        return

    def value_Gs():
        str1.set("G#")
        sound = pygame.mixer.Sound("C:\music\Music_Notes\G_s.wav")
        sound.play()
        return

    def value_Bd():
        str1.set("Bd")
        sound = pygame.mixer.Sound("C:\music\Music_Notes\Bb.wav")
        sound.play()
        return

    def value_Cs1():
        str1.set("Cs1")
        sound = pygame.mixer.Sound("C:\music\Music_Notes\C_s1.wav")
        sound.play()
        return

    def value_Ds1():
        str1.set("Ds1")
        sound = pygame.mixer.Sound("C:\music\Music_Notes\D_s1.wav")
        sound.play()
        return

    def value_C():
        str1.set("C")
        sound = pygame.mixer.Sound("C:\music\Music_Notes\C.wav")
        sound.play()
        return

    def value_D():
        str1.set("D")
        sound = pygame.mixer.Sound("C:\music\Music_Notes\D.wav")
        sound.play()
        return

    def value_E():
        str1.set("E")
        sound = pygame.mixer.Sound("C:\music\Music_Notes\E.wav")
        sound.play()
        return

    def value_F():
        str1.set("F")
        sound = pygame.mixer.Sound("C:\music\Music_Notes\F.wav")
        sound.play()
        return

    def value_G():
        str1.set("G")
        sound = pygame.mixer.Sound("C:\music\Music_Notes\G.wav")
        sound.play()
        return

    def value_A():
        str1.set("A")
        sound = pygame.mixer.Sound("C:\music\Music_Notes\A.wav")
        sound.play()
        return

    def value_B():
        str1.set("B")
        sound = pygame.mixer.Sound("C:\music\Music_Notes\B.wav")
        sound.play()
        return

    def value_C1():
        str1.set("C1")
        sound = pygame.mixer.Sound("C:\music\Music_Notes\C1.wav")
        sound.play()
        return

    def value_D1():
        str1.set("D1")
        sound = pygame.mixer.Sound("C:\music\Music_Notes\D1.wav")
        sound.play()
        return

    def value_E1():
        str1.set("E1")
        sound = pygame.mixer.Sound("C:\music\Music_Notes\E1.wav")
        sound.play()
        return



#

    Label(ABC1, text="Piano", font=('arial', 20, 'bold'), width=20,padx=8, pady=8,  bg="pink",
    fg="white", justify=CENTER).grid(row=0, column=0, columnspan=11)

    btnCs=Button(ABC2, height= 6, width=5, bd=4,text="도#",bg="black", fg="white", font=('arial', 15, 'bold'), command=value_Cs)
    btnCs.grid(row=0,column=0, padx=5, pady=5)
    btnDs=Button(ABC2, height= 6, width=5, bd=4, text="레#", bg="black", fg="white",font=('arial', 15, 'bold'), command=value_Ds)
    btnDs.grid(row=0,column=2, padx=5, pady=5)

    btnSpace2=Button(ABC2, state=DISABLED, width=2, height=6, bg="pink",relief=FLAT)
    btnSpace2.grid(row=0,column=3, padx=0, pady=0)

    btnFs=Button(ABC2, height= 6, width=5, bd=4, text="파#",  bg="black", fg="white", font=('arial', 15, 'bold'), command=value_Fs)
    btnFs.grid(row=0,column=4, padx=5, pady=5)
    btnGs=Button(ABC2,height= 6, width=5, bd=4, text="솔#",  bg="black", fg="white", font=('arial', 15, 'bold'), command=value_Gs)
    btnGs.grid(row=0,column=6, padx=5, pady=5)
    btnBb=Button(ABC2, height= 6, width=5, bd=4, text="라",  bg="black", fg="white", font=('arial', 15, 'bold'), command=value_Bd)
    btnBb.grid(row=0,column=8, padx=5, pady=5)

    btnSpace5 = Button( ABC2, state=DISABLED, width=2, height=6, bg="pink", relief=FLAT)
    btnSpace5.grid( row=0, column=9, padx=0, pady=0 )

    btnCs1=Button(ABC2, height= 6, width=5,bd=4, text="도#", bg="black", fg="white", font=('arial', 15, 'bold'), command=value_Cs1)
    btnCs1.grid(row=0,column=10, padx=5, pady=5)
    btnDs1=Button(ABC2, height= 6, width=5, bd=4, text="레#",bg="black",fg="white", font=('arial', 15, 'bold'), command=value_Ds1)
    btnDs1.grid(row=0,column=12, padx=5, pady=5)

    btnC = Button(ABC3, bd=4,height= 7, width=5, text="도", bg ="white", fg="black", font=('arial', 15, 'bold'), command=value_C)
    btnC.grid(row=0, column=0, padx=5, pady=5)
    btnD = Button(ABC3, bd=4, height= 7, width=5, text="레", bg ="white", fg="black", font=('arial', 15, 'bold'), command=value_D)
    btnD.grid(row=0, column=1, padx=5, pady=5)
    btnE = Button(ABC3, bd=4, height= 7, width=5, text="미", bg ="white", fg="black", font=('arial', 15, 'bold'), command=value_E)
    btnE.grid(row=0, column=2, padx=5, pady=5)
    btnF = Button(ABC3, bd=4, height= 7, width=5, text="파", bg ="white", fg="black", font=('arial', 15, 'bold'), command=value_F)
    btnF.grid(row=0, column=3, padx=5, pady=5)

    btnG = Button(ABC3, bd=4, height= 7, width=5, text="솔", bg ="white", fg="black", font=('arial', 15, 'bold'), command=value_G)
    btnG.grid(row=0, column=4, padx=5, pady=5)
    btnA = Button(ABC3, bd=4, height= 7, width=5, text="라", bg ="white", fg="black", font=('arial', 15, 'bold'), command=value_A)
    btnA.grid(row=0, column=5, padx=5, pady=5)
    btnB = Button(ABC3, bd=4, height=7, width=5, text="시", bg ="white", fg="black", font=('arial', 15, 'bold'), command=value_B)
    btnB.grid(row=0, column=6, padx=5, pady=5)
    btnC1 = Button(ABC3, bd=4,height= 7, width=5, text="도", bg ="white", fg="black", font=('arial', 15, 'bold'), command=value_C1)
    btnC1.grid(row=0, column=7, padx=5, pady=5)

    btnD1 = Button(ABC3, bd=4, height= 7, width=5, text="레", bg ="white", fg="black", font=('arial', 15, 'bold'), command=value_D1)
    btnD1.grid(row=0, column=8, padx=5, pady=5)
    btnE1 = Button(ABC3, bd=4, height= 7, width=5, text="미", bg ="white", fg="black", font=('arial', 15, 'bold'), command=value_E1)
    btnE1.grid(row=0, column=9, padx=5, pady=5)

piano.mainloop()