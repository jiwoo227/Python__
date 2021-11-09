from roboid import *

hamster = Hamster()

while True:
    key = Keyboard.read() # 키보드 이벤트를 얻는다.
    if key: # 키보드 이벤트가 있으면
        if key == 'a':
            hamster.note(Hamster.NOTE_C_4) # 도
        elif key == 's':
            hamster.note(Hamster.NOTE_D_4) # 레
        elif key == 'd':
            hamster.note(Hamster.NOTE_E_4) # 미
        elif key == 'f':
            hamster.note(Hamster.NOTE_F_4) # 파
        elif key == 'g':
            hamster.note(Hamster.NOTE_G_4) # 솔
        elif key == 'h':
            hamster.note(Hamster.NOTE_A_4) # 라
        elif key == 'j':
            hamster.note(Hamster.NOTE_B_4) # 시
        elif key == 'k':
            hamster.note(Hamster.NOTE_C_5) # 도
        elif key == 'l':
            hamster.note(Hamster.NOTE_D_5) # 레
        elif key == ';':
            hamster.note(Hamster.NOTE_E_5) # 미
        elif key == "'":
            hamster.note(Hamster.NOTE_F_5) # 파
        elif key == ' ': # 스페이스 키
            hamster.note(0) # 소리를 끈다.

    wait(20) # 너무 빨리 반복하지 않도록 한다.