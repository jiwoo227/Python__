from baseball_game_engine import make_quiz, check
from custom_error import InvalidCountError
answer = make_quiz()
# print(answer)
#숫자 3자리 중복없이 묻자
while True:
    player = input("숫자 세자리는?")
    try: #숫자가 아닐 때 에러 처리
        player_int = int(player)
    except ValueError:
        continue
        #길이가 3이 아닐 때 에러 처리
    if len(player) != 3:
        raise InvalidCountError("3자리가 아닙니다.")

#strike, ball 확인하자
    strike, ball = check(answer, player)
# 출력하자
    print(f'{player}\tstrike: {strike}\tball: {ball}')
# strike가 3일 때, 나가자
    if strike == 3:
        break


print('축하해')