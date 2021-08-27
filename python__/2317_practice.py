# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*3)
print(3*(3+1))

# 문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

# boolean 자료형
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 변수
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리 집" + animal + "의 이름은" + name + " 연탄이예요")
print(name + "는 " + str(age)+ "살이며, " +  hobby + "아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))

# 주석
''' 이렇게 
하면
여러문장이
주석처리
됩니다.'''

# Q1.1
# Quiz) 변수를 이용하여 다음 문장을 출력하시오.
#
# 변수명
# :station
#
# 변수값
# : "사당", "신도림", "인천공항" 순서대로 입력
#
# 출력문장
# : XX행 열차가 들어오고 있습니다.

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")

# 연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3)
print(5%3)
print(10%3)
print(5//3)
print(10//3)

print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)

print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)

print(1 != 3)
print(not(1 != 3))

print((3 > 0) and (3 < 5 ))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5))

print(5 > 4 > 3)
print(5 > 4 > 7)

# 간단한수식
print(2 + 3 * 4)
print((2 + 3) * 4)
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)

number %= 5
print(number)

# 숫자처리함수
print(abs(-5))
print(pow(4,2))
print(max(5,12))
print(min(5,12))
print(round(3.14))
print(round(4.99))

from math import *
print(floor(4.99))
print(ceil(3.14))
print(sqrt(16))

# 랜덤함수
from random import *
print(random())
print(random() * 10)
# print(int(random) * 10)
# print(int(random) * 10)
# print(int(random) * 10)
# print((int(random) * 10) + 1)
# print((int(random) * 10) + 1)
# print((int(random) * 10) + 1)
# print((int(random) * 10) + 1)
# print((int(random) * 10) + 1)

# print((int(random) * 45) + 1)
# print((int(random) * 45) + 1)
# print((int(random) * 45) + 1)
# print((int(random) * 45) + 1)
# print((int(random) * 45) + 1)
# print((int(random) * 45) + 1)

# print((int(random) * 46))
# print((int(random) * 46))
# print((int(random) * 46))
# print((int(random) * 46))
# print((int(random) * 46))
# print((int(random) * 46))

print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))


# Q2
# 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오
#
# 조건 1: 랜덤으로 날짜를 뽑아야 함
# 조건 2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건 3: 매원 1~3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

# 문자열
from random import *
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")

sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고, 
파이썬은 쉬워요"""
print(sentence3)

# 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])
print("뒤 7자리: " + jumin[7:])
print("뒤 7자리 : " + jumin[-7:1])

# 문자열처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java"))
print(python.index("Java"))
print("Hi")

print(python.count("n"))

print("a" + "b")
print("a", "b")

# 문자열포맷
# 방법 1
# print("나는 %살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이선")
# print("Apple 은 %c로 시작해요." % "A")
# %s
# print("나는 %s 살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
#
# 방법 2
# print("나는 {}살입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요." .format("파란","빨간"))
# print("나는 {0}색과 {1}색을 좋아해요." .format("파란","빨간"))
# print("나는 {1}색과 {2}색을 좋아해요." .format("파란","빨간"))
#
# 방법 3
# print("나는 {}살이며, {}색을 좋아해요." .format(age=20, color="빨간"))
# print("나는 {}살이며, {}색을 좋아해요." .format(color="빨간", age=20))
#
# 방법 4
# age = 20;
# color = "빨간"
# print(f"나는 {age}살이며, {color} 색을 좋아해요.")

# Q3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# ex) http://naver.com
# 규칙1: http:// 부분은 제외 => naver.com
# 규칙2: 처음 만나는 점 . 이후 부분은 제외 => naver
# 규칙3: 남은 글자 중 처음 세 자리+ 글자 객수 + 글자 내 'e' 갯수 + '!로 구성'
#
# url = "http://naver.com"
url="http://youtube.com"
my_str = url.replace("http://", "")
# print(my_str)
my_str = my_str[:my_str.index(".")]
# my_str[0:5] -> 0,5 직전까지, (0,1,2,3,4)
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e"))+"!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))
# 탈출문자
#
# \n : 줄바꿈
# print("백문이 불여일건\n백견이 불여일타")
#
# \" \' : 문장 내에서 따옴표
# 저는 "나도 코딩"입니다.
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")
# print("저는 \'나도코딩\'입니다.")
#
# \\ : 문장 내에서 \
#     print("C:\\Users\\Nadocoding\\Desktop\\pythonWorkspace>")
#
#     \r : 커서를 맨 앞으로 이동
# print("Red Apple\rpine")
#
# \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")
#
# \t : 탬
# print("Red\tAppple")

# 리스트 []
# 지하철 칸별로 10명, 20명, 30명

subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 조세호 사이에 태워봄
subway.insert(1,"정형돈")
print(subway)

# 지하철에 있는 사람들 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)
#
# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함꼐 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(mix_list)

# 사전
carbinet = {3:"유재석", 100:"김태호"}
print(carbinet[3])
print(carbinet[100])

print(carbinet.get(3))
print(carbinet[5])
print(carbinet.get(5))
print(carbinet.get(5, "사용가능"))
print("hi")

print(3 in carbinet)
print(5 in carbinet)

carbinet = {"A-3":"유재석", "B-100":"김태호"}
print(carbinet["A-3"])
print(carbinet["B-100"])

# 새 손님
print(carbinet)
carbinet["A-3"] = "김종국"
carbinet["C-20"] = "조세호"
print(carbinet)

# 간 손님
del carbinet["A-3"]
print(carbinet)

# key 들만 출력
print(carbinet.keys())

# value 들만 출력
print(carbinet.values())

# key, value 쌍으로 출ㄺ
print(carbinet.items())

# 목욕탕 폐점
carbinet.clear()
print(carbinet)

# 튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스")

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name,age,hobby)

(name,age,hobby) = ("김종국", 20, "코딩")
print(name,age,hobby)

# 세트
# 집합
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세호"}
python = set([])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java-python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# 자료 구조의 변경
# 커피숍

menu = {"커피", "우유", "주스"}
print(menu,type(menu))

menu = list(menu)
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

# Q) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 ㅗㅍ이기 위해 대글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추춤을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.
#
# 조건 1: 편의상 댓글은 20명이 작성하였고 아이디는 1~ 20이라고 가정
# 조건 2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건 3: random 모듈의 shuffle 과 sample 을 활용
#
# (출력 예제)
# --당첨자 발표--
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# --축하합니다.--
#
#          (활용예제)
#
# from random import *
# 1st = [1,2,3,4,5]
# print[1st]
# shuffle(1st)
# print(1st)
# print(sample(1st,1))

from random import *
users = range(1,21)
# print(type(users))
users = list(users)
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users,4)

print("===당첨자 발표")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("축하합니다.")

# IF

# weather = input("오늘 날씨는 어떄요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요없어요.")

temp = int(input("기온은 어때요?"))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요.")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요.")

# for

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

# while

customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")

#continue와 break

absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break;
    print("{0}, 책을 읽어봐.".format(student))

# 한 줄 for

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
# students  = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)
#
# 학생 이름을 길이로 변환
# students = ["Iron man", "I am groot"]
# students = [lens(i) for i in students]
# print(students)
#
# 학새이름을 대문자로 변환
students = ["Iron man", "I am groot"]
students = [i.upper() for i in students]
print(students)

# Quiz 5

# 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다
# 50명의 승객과 매칭 기화가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오
#
# 조건 1: 승객별 운행 소요 시간은 5분 ~ 10분 사이의 난수로 정해집니다.
# 조건 2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
#
# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [] 50번째 손님 (소요시간 : 16분)
#
# 총 탑승 승객  :2분

from random import *
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간:{1}분)".format(i, time))
        cnt += 1
    else:
        print("[O] {0}번째 손님 (소요시간:{1}분)".format(i, time))


print("총 탑승 승객 : {0} 분".format(cnt))

# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

# 전달값과 반환값
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance+money))
    return balance + money
def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance
def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance  = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission,balance))

# 기본값

def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용언어: {2}" \
          .format(name, age, main_lang))

profile("유재석")
profile("김태호")

# 키워드값

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")

# 가변 인자

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end="")
    print(lang1, lang2, lang3, lang4, lang5)

def profile(name,age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end="")
    for lang in language:
        print(lang, end="")
    print()

profile("유재석", 20, "Python", " Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotilin", "Swift")

# 지역변수와 전역변수

gun = 10

def checkpoint(soldiers):
    global  gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun
print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

# Quiz 6

# 표준 체중ㅇ을 구하는 프로그램을 작성하시오.
#
# 표준 체중 : 각 개인의 키에 적당한 체중
#
# (성별에 따른 공식)
# 남자 : 키 (m) x 키(m) x 22
# 여자 : 키 (m) x 키(m) x 21
#
# 조건 1: 표준 체중은 별도의 함수 내에서 계산
# 함수명 : std_weight
# 전달값 : 키 (height), 성별(gender)
# 조건 2: 표준 체중은 소수점 둘째자리에까지 표시
#
# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 32
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2} kg 입니다.".format(height, gender, weight))


# 클래스
# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력{0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 멤버 변수
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력{0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대에게 보이지 않음)
wraith1= Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 50)
wraith2.clocking =True

if wraith1.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# 메소드
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
.format(self.name, location, self.damage))
        def damaged(self,damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

#메딕 : 의무병

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 == AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

#상속

# 일반 유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        slef.damage = damage

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
.format(self.name, location, self.damage))
        def damaged(self,damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

#메딕 : 의무병

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 == AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 다중 상속
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        slef.damage = damage

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
.format(self.name, location, self.damage))
        def damaged(self,damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃, 탱크 등을 수송, 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

        def fly(self, name, lacation):
            print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
                  .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flaying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flaying_speed)


# 메서드 오버라이딩

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]")\
            .format(self.name, location, self.speed)

# 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, speed,damage, flying_speed):
        Unit.__init__(self, name, hp, speed)
        slef.damage = damage

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
.format(self.name, location, self.damage))
        def damaged(self,damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

#메딕 : 의무병

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 == AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 다중 상속
# 일반 유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp

# 공격 유닛
class Attack(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        slef.damage = damage

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
.format(self.name, location, self.damage))
        def damaged(self,damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃, 탱크 등을 수송, 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

        def fly(self, name, lacation):
            print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
                  .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flaying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flaying_speed)

# 발키리 : 공중 공격 유닛, 한 번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(varkyrie.name, "3시")

# 메서드 오버라이딩

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]")\
            .format(self.name, location, self.speed)

# 공격 유닛
class Attack(Unit):
    def __init__(self, name, hp,speed, damage):
        Unit.__init__(self, name, hp, speed)
        slef.damage = damage

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
.format(self.name, location, self.damage))
        def damaged(self,damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃, 탱크 등을 수송, 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

        def fly(self, name, lacation):
            print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
                  .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flaying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flaying_speed)

        def move(self, location):
            print("[공중 유닛 이동]")
            self.fly(self.name, location)

#벌쳐 : 지상 유닛, 기동성이 좊음
vulture = AttackUnit("벌쳐", 80, 10, 20)

#배틀크루저 : 공중 유닛, 체력 좊음, 공격력 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
#battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시시")


#super
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]")\
            .format(self.name, location, self.speed)

# 공격 유닛
class Attack(Unit):
    def __init__(self, name, hp,speed, damage):
        Unit.__init__(self, name, hp, speed)
        slef.damage = damage

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
.format(self.name, location, self.damage))
        def damaged(self,damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃, 탱크 등을 수송, 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

        def fly(self, name, lacation):
            print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
                  .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flaying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flaying_speed)

        def move(self, location):
            print("[공중 유닛 이동]")
            self.fly(self.name, location)

#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

#서폴라이 디폿 : 건물, 1개 건물 = 8 유닛
supply_depot = BuildingUnit("서폴라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다")

def game_over():
    pass

game_start()
game_over()

#super
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]")\
            .format(self.name, location, self.speed)

# 공격 유닛
class Attack(Unit):
    def __init__(self, name, hp,speed, damage):
        Unit.__init__(self, name, hp, speed)
        slef.damage = damage

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
.format(self.name, location, self.damage))
        def damaged(self,damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃, 탱크 등을 수송, 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

        def fly(self, name, lacation):
            print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
                  .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flaying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flaying_speed)

        def move(self, location):
            print("[공중 유닛 이동]")
            self.fly(self.name, location)

#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location


class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)


#드랍쉽
dropship = FlyableUnit()

#스타크래프트 전반전

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]")\
            .format(self.name, location, self.speed)

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp,speed, damage):
        Unit.__init__(self, name, hp, speed)
        slef.damage = damage

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
.format(self.name, location, self.damage))
        def damaged(self,damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

#마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린", 40, 1, 5)

        #스팀팩 : 일정 시간 동안 어둠 및 공격 속도를 증가, 체력 10 감소
        def stimpack(self):
            if self.hp > 10:
                self.hp -= 10
                print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
            else:
                print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
#탱크
class Tank(AttackUnit):
    #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동 불가.
    seize_developed = False #시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)

    def set_seize_mode(self):
        if Tank.seize_developed == false:
            return

        #현재 시즈모드가 아닐 때 -> 시즈모드
        if self.set_seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        #현재 시즈모드일 떄 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

#날 수 있는 기능을 가진 클래스

# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃, 탱크 등을 수송, 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

        def fly(self, name, lacation):
            print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
                  .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flaying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flaying_speed)

        def move(self, location):
            print("[공중 유닛 이동]")
            self.fly(self.name, location)


#레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

        def clockint(self):
            if self.clocked == True:
                print("{0} : 클로킹 모드 해제합니다.".format(self.name))
                self.clocked = False

            else:
                print("{0} : 클로킹 모드 설정합니다.".format(self.name))
                self.clocked = True

#스타크래프트 후반전

from random import *
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]")\
            .format(self.name, location, self.speed)

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp,speed, damage):
        Unit.__init__(self, name, hp, speed)
        slef.damage = damage

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
.format(self.name, location, self.damage))
        def damaged(self,damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

#마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린", 40, 1, 5)

        #스팀팩 : 일정 시간 동안 어둠 및 공격 속도를 증가, 체력 10 감소
        def stimpack(self):
            if self.hp > 10:
                self.hp -= 10
                print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
            else:
                print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
#탱크
class Tank(AttackUnit):
    #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동 불가.
    seize_developed = False #시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)

    def set_seize_mode(self):
        if Tank.seize_developed == false:
            return

        #현재 시즈모드가 아닐 때 -> 시즈모드
        if self.set_seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        #현재 시즈모드일 떄 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

#날 수 있는 기능을 가진 클래스

# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃, 탱크 등을 수송, 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

        def fly(self, name, lacation):
            print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
                  .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flaying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flaying_speed)

        def move(self, location):
            print("[공중 유닛 이동]")
            self.fly(self.name, location)


#레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

        def clockint(self):
            if self.clocked == True:
                print("{0} : 클로킹 모드 해제합니다.".format(self.name))
                self.clocked = False

            else:
                print("{0} : 클로킹 모드 설정합니다.".format(self.name))
                self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Plyyer : gg")
    print("[Plyer] 님이 게임을 나갔습니다.")

#실제 게임 진행
game_start()

#마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 - Marine()

#탱크 2기 생성
t1 = Tank()
t2 = Tank()

#레이스 1기 생성
w1 = Wraith()

#유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

#공격 모드 준비 (마린: 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit,Marine):
        unit.stimpack()

    elif isinstance(unit, Tank):
        unit.set_seize_mode()

    elif isinstance(unit, Wraith):
        unit.clocking()

#전군 공격
for unit in attack_units:
    unit.attack("1시")

#전군 피해
for unit in attack_units:
    unit.damaged(radint(5,20))

#퀴즈

class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

        #매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type\
              , self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house1 = House("마포", "오피스텔", "전세", "5억", "2007년")
house1 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()



































