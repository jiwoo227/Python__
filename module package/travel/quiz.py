
# 1. 핸드폰 요금이 62421원 나왔다. 100원 미만은 절사한다고 한다. 62400원 청구. 59827원일 경우, 실제 청구 금액은?

import math

bill = 62421
print(bill//100*100)  #624*100
print(bill-bill%100)  #62421 - 100
print(math.floor(bill/100)*100)
#2. 평가계획은 100점 만점에 10점 단위로 점수를 줄 수 있다. 채점한 결과 93점이 나왔다. 90점 부여. 56점은 몇 점 부여?
score = 93
score = 56
print(round(score/10)*10)
print(round(score, -1))
# 3. 로또 복권 자동 생성기를 만든다면?
# (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)
import random
print(random.sample(range(1,45),6))

# 4. 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?(185:O, 212:X)
list_r = random.sample(range(1,9 +1), 3)
print("". join(str(n) for n in list_r))
print("". join(map(str, list_r)))
string = ''
for n in list_r:
    string += str(n)
print(string)

# 5. 내가 태어난 날로부터 며칠이 지났는지?
import datetime
now = datetime.datetime.now()
print(now)
birthday = datetime.datetime(2004, 2, 27, 11,3)
print(now - birthday)

# 6. 올해 크리스마스까지 며칠이 남았는지?
now1 = datetime.datetime.now()
chrismas = datetime.datetime(2021,12,25)
how = chrismas - now
day = how.days


print('크리스마스는 {}일 남았습니다.'.format(day))
# 7. 내 생일이 며칠 남았는지?
my_birthday = datetime.datetime(2022,2,27)
print(my_birthday - now)



print('지우의 생일은 {}일  남았습니다.'.format(day))
# 8. 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?
# 마지막 번호가 몇 번인지 묻자
last_number = input("마지막 번호는? ")
# 1~마지막 번호까지 리스트 만들자
list_class= list(range(1, int(last_number)+ 1 ))
print(list_class)
#무한 반목
while True:
#나간 친구 번호 묻자

   exclude_number = input("벨 번호는? ( 그냥 enter치면 종료")
    if exclude_number =='':
        break
#리스트에서 뺴자
    list_class.remove(int(exclude_number))
#그냥 enter면 반복 끝내자
#랜덤으로 섞자
random.shuffle(list_class)
#print(list_class)
print('자리\t학생번호')
#출력하자
for index, n in enumerate(list_class):
    print(f'{index+1}\t{n}')