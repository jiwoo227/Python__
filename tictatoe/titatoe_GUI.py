import tkinter
from tictatoe_game_engine import TictatoeGameEngine

class TictatoeGUI:
    def __init__(self):
        self.game_engine = TictatoeGameEngine()
        self.init_GUI()

    def init_GUI(self):
        self.CANVAS_SIZE = 300
        self.root = tkinter.Tk() #mainloop와 같이 윈도우 창을 나타냄
        self.root.title('틱택토')
        self.root.geometry(f'{self.CANVAS_SIZE}x{self.CANVAS_SIZE}')
        self.root.resizable(width=False, height=False)

        self.canvas = tkinter.Canvas(self.root, bg='white', width=self.CANVAS_SIZE, height=self.CANVAS_SIZE)
        self.canvas.pack()

        self.images ={} # {'X' : PhotoImage객체, 'O' : PhotoImgae객체}
        self.images['X'] = tkinter.PhotoImage(file='X.gif')
        self.images['X'] = tkinter.PhotoImage(file='O.gif')

        self.canvas.bind('<Button-1>', self.click_handler)
        #click_handler 뒤에 ()가 없다는건 지금 실행하는게 아님 ()가 있으면 지금 실행하는것

        self.root.mainloop()

    def click_handler(self, event):
        #print(event.x, event.y) click 위치 설정
        #input event.x,evetn.y -> row,col
        row,col = self.coordinate_to_position(event.x, event.y)
        #set row,col
        self.game_engine.set(row,col)
        #show board
        self.game_engine.show_board()
        #승자가 있거나 무승부일 때 게임오버, 결과 출력하기
        #change turn


    def draw_board(self):
        pass

    def coordinate_to_position(self,x, y):
       pass
if __name__ == '__main__':
    ttt_GUI = TictatoeGUI()