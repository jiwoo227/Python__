from baseball_game_engine import make_quiz, check

answer = make_quiz()
# print(answer)
#숫자 3자리 중복없이 묻자
while True:
    player = input("숫자 세자리는?")
#strike, ball 확인하자
    strike, ball = check(answer, player)
# 출력하자
    print(f'{player}\tstrike: {strike}\tball: {ball}')
# strike가 3일 때, 나가자
    if strike == 3:
        break


print('축하해')