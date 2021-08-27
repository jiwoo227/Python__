from diaryNote import DiaryNote
from time import sleep

def print_menu():
    print("\n     𝑃𝑅𝐴𝐼𝑆𝐸 𝑁𝑂𝑇𝐸")
    print("│﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀")
    print("│  Ⅰ. 일기 작성")
    print("│  Ⅱ. 일기 불러오기")
    print("│  Ⅲ. 일기 수정")
    print("│  Ⅳ. 일기 삭제")
    print("│  Ⅴ. 모든 일기")
    print("│  Ⅵ. 통계")
    print("│  Ⅶ. 종료")
    print("└——————— - [ 📼 ]. + ")

    print("\n╭────────────────✎")
    print("| 메뉴를 선택하세요")
    menu = input("╰─▗ ▘➤ ")
    return menu


def main():
    praisenote = DiaryNote()
    while True:
        menu = print_menu()
        if menu == '1':
            # 일기 작성
            praisenote.write()
        elif menu == '2':
            # 일기 불러오기
            praisenote.loading()
        elif menu == '3':
            praisenote.revise()
            # 일기 수정하기
        elif menu == '4':
            praisenote.delete()
            # 일기 삭제하기
        elif menu == '5':
            praisenote.show_all_diary()
            # 모든 일기 보기
        elif menu == '6':
            praisenote.statistics()
            # 통계
        elif menu == '7':
            # print("\n     종료되었습니다.  ")
            # print("＼＿＿＿＿＿＿＿＿＿＿＿／")
            # print("　　ｏ")
            # print("　　 。")
            # print("　　　｡")
            # print("　　∧＿∧")
            # print("　 (*　･ω･)")
            # print("＿(__つ/￣￣￣/_")
            # print("　　＼/　　　/")

            print("\n  ♡ ∩_∩")
            print("  （„• ֊ •„)♡")
            print(" ┏━━━━∪∪━━━━━━━━━━━━━━━━━┓")
            print(" ♡ 𝚃𝚑𝚊𝚗𝚔 𝚈𝚘𝚞 𝙵𝚘𝚛 𝙿𝚕𝚊𝚢𝚒𝚗𝚐! ♡")
            print(" ┗━━━━━━━━━━━━━━━━━━━━━━━━┛")
            break
            # 종료
        else:
            print("\n   /)⋈/)")
            print("  (｡•ㅅ•｡)♡")
            print(" ┏--∪-∪━━━━━━━━━━━━━━┓")
            print(" ♡ 다시 입력하세요! *.。♡")
            print(" ┗-━━━━━━━━━━━━━━━━━━━┛")
            sleep(1)

if __name__ == '__main__':
    main()

