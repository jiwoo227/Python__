#숫자야구게임
#퀴즈내자 숫자 3자리 중복없이
import random
def make_quiz():
#무한 반복
    list_r = random.sample(range(1,9 + 1), 3)
    string_number = "".join(map(str, list_r))

    return string_number

def check(answer, player):
    strike = 0
    ball = 0
    for j, p in enumerate(player):
        for i, a in enumerate(answer):
            if p == a:
                for i ==j:
                    strike += 1
                else:
                    ball += 1
        player[0] == answer[0]
        player[0] == answer[1]
        player[0] == answer[2]
        player[1] == answer[0]
        player[1] == answer[1]
        player[1] == answer[2]
        player[2] == answer[0]
        player[2] == answer[1]
        player[2] == answer[2]

    #번호가 있고, 자리가 다르면 ball += 1
    return strike, ball


if __name__ == '__main__':
    answer = make_quiz()
    print(answer)
    strike, ball = check("421","227")
    print(strike, ball)  #1, 0
    strike, ball = check("231", "124")
    print(strike, ball)
