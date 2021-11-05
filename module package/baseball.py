from baseball_game_engine import make_quiz, check
answer = make_quiz()
# print(answer)
#숫자 3자리 중복없이 묻자
count = 0


def save_history(player, count):
    with open('baseball_history.txt', 'w')as f:
        f.write(f'{player}\t{count}\n')

def load_history():
    count_list = []
    with open('baseball_history.txt' 'r') as f:
        while True:
            line = f.readline()
            if line == '':
                break

            line_data = line.rstrip().split('\t')
            print(line_data[1])
    count_list = set(count_list)
    count_list = list(count_list)
    count_list.sort()
    print(count_list[:3])

print(answer)
while True:
    player = input("숫자 세자리는?(t: top3)")
    if player == 't':
        try:
            history = load_history()
        expect FileNotFoundError:
            print('history 파일 없음')
            continue
        print(history)
        continue
    try: #숫자가 아닐 때 에러 처리
        player_int = int(player)
    except ValueError:
        continue
        #길이가 3이 아닐 때 에러 처리
    if len(player) != len(answer):
        #raise InvalidCountError("3자리가 아닙니다.")
        print(f'입력한 숫자의 개수가 정답과 다릅니다.정답 :{len(answer)} 3글자')
        continue
#strike, ball 확인하자
    count += 1
    strike, ball = check(answer, player)
# 출력하자
    print(f'{player}\tstrike: {strike}\tball: {ball}\t{count}t')
# strike가 3일 때, 나가자
    if strike == 3:
        save_history(player, count)
        
        break


print('축하해')