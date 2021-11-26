import tkinter as ttk
from tkinter import *
from tkinter import messagebox
import pygame

piano = Tk()
piano.title('피아니스트')
piano.geometry('350x300+0+0')
pygame.init()
from tkinter import messagebox as msg


def btn_click():
    piano = ttk.Toplevel()
    piano.geometry( '350x300+0+0' )
    label1 = Label(piano, text='둘 중에 원하는 것을 선택해줘!' )
    label1.pack()
    btn2 = Button( piano, width=9, height=5, text="피아노치기", bg="black", fg="white", command=piano1)
    btn2.pack()
    btn3 = Button(piano, width=9, height=5, text="악보보기", bg="black", fg="white", command=btn1_click)
    btn3.pack()

    btn2.place( x=100, y=100 )
    btn3.place( x=200, y=100 )
    label1.place( x=105, y=50 )

def btnn_click():
    msg.showwarning('안돼!', '좋아를 눌러야 돼!!')


label = Label(piano, text=' 피아니스트가 되어보자!')
label.pack()
btn1=Button(piano, width=9, height=5, text="좋아!", bg="black", fg="white", command=btn_click)
btn1.pack()
btn4=Button(piano, width=9, height=5, text="음..별로!", bg="black", fg="white",  command=btnn_click)
btn4.pack()

label.place(x=110, y=50)
btn1.place( x=100, y=100 )
btn4.place( x=200, y=100 )

def btn1_click():
    piano = ttk.Toplevel()
    piano.geometry( '370x300+0+0' )

    label1 = Label(piano, text='보고 싶은 악보를 골라봐!' )
    label1.pack()
    btn1 = Button( piano, width=8, height=4, text="곰\n세마리", bg="black", fg="white", command=text1)
    btn1.pack()
    btn2 = Button( piano, width=8, height=4, text="나비야", bg="black", fg="white", command=text2)
    btn2.pack()
    btn3 = Button(piano, width=8, height=4, text="비행기", bg="black", fg="white", command=text3)
    btn3.pack()
    btn4 = Button( piano, width=8, height=4, text="생일\n축하\n노래", bg="black", fg="white", command=text4)
    btn4.pack()
    btn5 = Button( piano, width=8, height=4, text="학교종이\n땡땡땡", bg="black", fg="white", command=text5)
    btn5.pack()
    btn6 = Button( piano, width=8, height=4, text="햇볕은\n쨍쨍", bg="black", fg="white", command=text6)
    btn6.pack()
    btn7 = Button( piano, width=8, height=4, text="나의\n악보", bg="black", fg="white", command=textt)
    btn7.pack()
    btn8 = Button( piano, width=8, height=4, text="악보\n직접\n쓰기", bg="black", fg="white", command= songinput)
    btn8.pack()
    btn9 = Button(piano, width=5, height=1, text="눌러봐!",bg="black", fg="white")

    btn1.place(x=30, y=100)
    btn2.place( x=110, y=100 )
    btn3.place( x=190, y=100 )
    btn4.place( x=270, y=100 )
    btn5.place( x=30, y=200 )
    btn6.place( x=110, y=200 )
    btn7.place( x=190, y=200 )
    btn8.place( x=270, y=200 )
    btn9.place( x=300, y=10 )
    label1.place( x=120, y=40 )

def text1():
    piano = ttk.Toplevel()
    piano.geometry( "300x300" )

    label = Label( piano, text="곰 세마리\n", font=(15) )
    label.pack()
    label1 = Label( piano,text="계이름\n\n도 도도도 도 미 솔솔미 도 솔솔미 솔솔미 도도도\n솔 솔 미 도 솔 솔 솔 솔 솔 미 도 솔 솔 솔\n 솔 솔 미 도 솔솔솔라솔 도 솔 도 솔 미레도\n\n" )
    label1.pack()
    label1 = Label( piano, text="번호\n\n11223333" )
    label1.pack()


def text2():
    piano = ttk.Toplevel()
    piano.geometry( "300x300" )

    label = Label( piano, text="나비야\n", font=(15) )
    label.pack()
    label1 = Label( piano,text="계이름\n\n솔 미 미 파 레 레 도레미파 솔 솔 솔\n솔 미 미 미 파레레 도미솔솔 미 미 미\n\n" )
    label1.pack()
    label1 = Label( piano, text="번호\n\n11223333" )
    label1.pack()


def text3():
    piano = ttk.Toplevel()
    piano.geometry( "300x300" )

    label = Label( piano, text="비행기\n", font=(15) )
    label.pack()
    label1 = Label( piano, text="계이름\n\n미 레도 레 미 미 미 레 레 레 미 솔 솔\n미 레도 레 미 미 미 레 레 미 레 도\n\n" )
    label1.pack()
    label1 = Label( piano,text="번호\n\n11223333" )
    label1.pack()

def text4():
    piano = ttk.Toplevel()
    piano.geometry( "300x300" )

    label = Label( piano, text="생일 축하 노래\n", font=(15) )
    label.pack()
    label1 = Label( piano,text="계이름\n\n도도레 도 파파미 도도레 도 솔솔파\n도 라 파 미 레 세세라 파 솔 솔라\n\n" )
    label1.pack()
    label1 = Label( piano, text="번호\n\n11223333" )
    label1.pack()


def text5():
    piano = ttk.Toplevel()
    piano.geometry( "300x300" )

    label = Label( piano, text="학교 종이 땡땡떙\n", font=(15) )
    label.pack()
    label1 = Label( piano,text="계이름\n\n솔솔 라라 솔솔 미 솔솔 미미 레\n 솔솔 라라 솔솔 미 솔 미 레 미 도\n\n" )
    label1.pack()
    label1 = Label( piano, text="번호\n\n11223333" )
    label1.pack()


def text6():
    piano = ttk.Toplevel()
    piano.geometry( "300x300" )

    label = Label( piano, text="햇볕은 쨍쩅\n", font=(15) )
    label.pack()
    label1 = Label( piano,text="계이름\n\n도미솔 솔 솔 미라솔미 도도\n도시도라솔라솔라 도시도라솔라솔라\n 라 라 솔 솔 미 미 솔 솔 레도레미 도 도\n\n" )
    label1.pack()
    label1 = Label( piano, text="번호\n\n11223333" )
    label1.pack()


def textt():
    piano = ttk.Toplevel()
    piano.geometry( "270x240" )
    f = open ("song.txt",'r', encoding="utf-8")
    text=f.read()

    label = ttk.Label(piano, text = text)
    label.pack()


def songsave(text):
    f = open('song.txt','a', encoding="utf-8")
    f.write(text+"\n")
    msg.showwarning( '저장완료', '저장되었습니다' )
    # piano.songinput.destroy()

def songinput():
    piano = ttk.Toplevel()
    piano.geometry("270x240")
    str = StringVar()

    label = Label(piano, text = "너만의 악보를 적어봐! ", font=(10))
    label.pack()
    textbox = Entry(piano,width=25, textvariable=str)
    textbox.pack()

    button_put = ttk.Button(piano, height=1, width=6, text="저장하기",command=lambda:songsave(str.get()))
    button_put.pack()


    label.place(x=50, y=50)
    textbox.place(x=20, y=80)
    button_put.place(x=200, y=76)








# def btn2_click():
#
#     piano = ttk.Toplevel()
#     piano.geometry( '350x300+0+0' )
#     label1 = Label( piano, text='치고싶은 피아노를 선택해줘!' )
#     label1.pack()
#     btn2 = Button( piano, width=9, height=5, text="1번 피아노", bg="black", fg="white", command=piano1)
#     btn2.pack()
#     btn3 = Button( piano, width=9, height=5, text="2번 피아노", bg="black", fg="white", command=ppiano)
#     btn3.pack()
#
#     btn2.place( x=100, y=100 )
#     btn3.place( x=200, y=100 )
#     label1.place( x=110, y=50 )

def piano1():
    piano = ttk.Toplevel()
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


# def ppiano():
#     piano = ttk.Toplevel()
#     piano.geometry( '345x345+0+0' )
#     str1 = StringVar()
#     str1.set( "Piano" )
#
#
#     def value_E1():
#         str1.set( "Piano" )
#         sound = pygame.mixer.Sound( "C:\music\Music_Notes\E1.wav" )
#         sound.play()
#         return
#
#     def key_7():
#         button7 = ttk.Button( piano, text="7", width=15, height=7, command=value_E1)
#         button7.grid( row=1, column=0 )
#
#     def key_8():
#         button8 = ttk.Button(piano, text="8", width=15, height=7, command=value_E1)
#         button8.grid( row=1, column=1 )
#
#     def key_9():
#         button9 = ttk.Button( piano, text="9" , width=15, height=7, command=value_E1)
#         button9.grid( row=1, column=2 )
#
#     def key_4():
#         button4 = ttk.Button( piano, text="4" , width=15, height=7, command=value_E1)
#         button4.grid( row=2, column=0 )
#
#     def key_5():
#         button5 = ttk.Button( piano, text="5", width=15, height=7, command=value_E1)
#         button5.grid( row=2, column=1 )
#
#     def key_6():
#         button6 = ttk.Button( piano, text="6", width=15, height=7, command=value_E1)
#         button6.grid( row=2, column=2 )
#
#     def key_1():
#         button1 = ttk.Button( piano, text="1" , width=15, height=7, command=value_E1)
#         button1.grid( row=3, column=0 )
#
#     def key_2():
#         button2 = ttk.Button(piano, text="2", width=15, height=7, command=value_E1)
#         button2.grid( row=3, column=1 )
#     def key_3():
#         button3 = ttk.Button( piano, text="3" , width=15, height=7, command=value_E1)
#         button3.grid( row=3, column=2 )


piano.mainloop()