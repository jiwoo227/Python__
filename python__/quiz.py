# 3-1

id_number = "040227"
print(id_number[0:2])
print(id_number[2:6])
print(int(id_number[:2])*int(id_number[2:]))



# # 3-2
# phone_number = "02-9872-6543"
# phone_number2 = "852-9872-6543"
# x = phone_number.index('-')
# # index() 없으면 valueError, find() 없으면 -1
# print(phone_number[0:2])
# print(phone_number[-4:])

# 전화번호 입력시 -가 있는, -가 없는
# phone_number1 = '018-2233-4353'
# phone_number3 = '018 2232 3232'
#
# phone_number = phone_number3
# result = ph.replace('-','').replace(' ','')
# print(result)

# 2-1
#학번을 student_number변수에 넣고, 학급을 출력하고, 학과를 출력하기
#반이 0미만이거나 7이상이면 "잘못입력했습니다."출력하기
#student_number ='2100' 또는 '2000'
#<출력예시>   1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.
# student_number='2317'
# if student_number[1]=="1":
#     print("1반 뉴미디어소프트웨어과")
# elif student_number[1]=="2":
#     print("2반 뉴미디어소프트웨어과")
# elif student_number[1]=="3":
#     print("3반 뉴미디어웹솔루션과")
# elif student_number[1]=='4':
#     print("4반 뉴미디어웹솔루션과")
# elif student_number[1]=='5':
#     print("5반 뉴미디어디자인과")
# elif student_number[1]=="6":
#     print("6반 뉴미디어디자인과")
# else:print("잘못입력했습니다.")
#
# major=['0', '뉴미디어소프트웨어과','뉴미디어웹솔루션과','뉴미디어디자인과']
# if 1 <= number <= 6:
#     print(f'{number}반 {ma}ors{[(number-1) // 2]}')
# else:
#     print("잘못입력했습니다.")


#2-2
#학번을 함수인 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
#함수호출
#grade, major = get_major("2100")
#print(major,grade) #뉴미디어소프트웨어과2
def get_major(argumenet):
    if argumenet[1]=="1" or argumenet[1]=="2":
        major="뉴미디어소프트웨어과"
        return argumenet[0],major
    elif argumenet[1]=="3" or argumenet[1]=="4":
        major="뉴미디어웹솔루션과"
        return argumenet[0],major
    elif argumenet[1]=="5" or argumenet[1]=="6":
        major="뉴미디어디자인과"
        return argumenet[0],major

grade,major=get_major("2411")
print(major,grade)

#3-3
#인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면
#그 인수들의 평균을 구하여 리턴하는 함수 만들기
#<함수호출>
#print(average(10,20,30)) #20.0
#print(average(4,23)) #13.5

def average(*number):
    sum=0
    for i in number:
        sum+=i

    average=(sum/len(number))
    print(average)


print(average(10,20,30,40,50))

def average(*numbers):
    sum_value = 0
    count = 0
    for number in numbers:
        sum_value += number
        count += 1
    return sum_value / count

print(average(10, 20, 30))      #(10,20,30) == > numbers
print(average(4, 23))           #(4,23) ===> numbers


#2-4
#키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI지수를 리턴하는 함수 만들기
#(소수 첫째자리까지 반올림)

#*BMI지수 계산법 : 체중(kg) / 키의 제곱
#18.5 미만 : 저체중
#18.5이상 23 미만 : 보통
#23 이상 25 미만 : 과체중
#25이상 : 비만

#<함수호출>
#bmi = get_bmi(176,69)
#print(bmi) #22.3

def get_bmi(height, weight):
    height/=100
    bmi=round((weight/(height*height)),1)
    if bmi>18.5:
        return "저체중"
    elif bmi>=18.5 and bmi<23:
        return "보통"
    elif bmi>=23 and bmi<25:
        return "과체중"
    elif bmi >25:
        return "비만"

bmi=get_bmi(176,69)
print(bmi)


def get_bmi(height, weight):
    height /= 100
    return round(weight / (height ** 2), 1)


bmi = get_bmi(164,31)
# print(bmi)
if bmi < 18.5:
    print('저체중')
elif 18.5<= bmi < 23:
    print('정상')
elif 23 <= bmi < 25:
    print('과체중')
elif 25 <= bmi:
    print('비만')

# 7단 출력하기
for i in range(1, 10): #i : 1~
    print(f'7 x {i} = {7* i}')

# 2~9단 출력하기
for dan in range(2, 10):
    for i in range(1, 9 + 1): #i : 2~9
        print(f'{dan} x {i} = {dan* i}')
    print('-' *10)

#    2~7단 출력하기
for dan in range(2, 9 + 1): #i : 1~9
    for i in range(1, 9 +1):
        print(f'{dan} x {i} = {dan* i}')
    print('-' *10)
    if dan == 7:
        break

#    구구단 2~7단을 출력하되 x1, x3, x5, x7, x9 인 것만 출력하기
for dan in range(2, 9 + 1): #i : 1~9
    for i in range(1, 9 +1):
        if i % 2 ==0:# if i == 2 or i == 4 or i ==6 or i == 8:
            continue
        print(f'{dan} x {i} = {dan* i}')
    print('-' *10)
    if dan == 7:
        break


# 3-1
def n_sum(n):
    new = str(n)       #new = "408"
    add = 0
    if n >= 1000000000:
        return -1
    for i in range(len(new)):   #len = 3  range(3) = 0,1,2
        add += int(new[i])  # new[0] = "4" new[1] = "0" new[2] = "8"
    return add

result = n_sum(10)
print(result)        #1
result = n_sum(331)
print(result)         #7
result = n_sum(408)
print(result)         #12
result = n_sum(1000000000)
print(result)         #-1
result = n_sum(10000000000)
print(result)         #-1


# 3-2
# Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
# * 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
def get_subway_fare(distance):
    if distance <= 10:
        return 720
    elif distance <= 50:
        add = (distance - 10) // 5 * 100
        if (distance - 10) % 5 > 0:
            add += 100
        return 720 + add
    elif distance > 50:
        add = (distance - 50) // 8 * 100
        if (distance - 50) % 8 > 0:
            add += 100
        return 720 + (50 - 10) // 5 * 100 + add

get_subway_fare(26)
fare = get_subway_fare(5)
print(fare)
fare = get_subway_fare(26)
print(fare)
fare = get_subway_fare(61)
print(fare)

# 3-3
def get_three_six_nine(i):
    str_i = str(i)  #str_i = "36"
    count_369 = 0
    for x in str_i: #x="3" x="6"      for x in "36":
        if (x == '3') or (x == '6') or (x == '9'):
            count_369 += 1
    if count_369 == 0:
        return (i)
    else:
        return (count_369 * '짝')


result = get_three_six_nine(1)
print(result)  # 1
result = get_three_six_nine(3)
print(result)  # 짝
result = get_three_six_nine(16)
print(result)  # 짝
result = get_three_six_nine(36)
print(result)  # 짝짝


# 3-4


# input값을 넣어 다음 날로 출력되게 하시오.
month = int(input())
day = int(input())

if month == 2 and day == 28:
    month += 1
    day = 1

elif (month == 4 or 6 or 9 or 11) and day == 30:
    month += 1
    day = 1
elif (month == 1 or 3 or 5 or 7 or 8 or 10 or 12) and day == 31:
    month += 1
    day = 1
else:
    day += 1

print(month)
print(day)

#Quiz 4-1
# [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
#is_prime() 함수를 만든다.
#인수로 1개의 숫자를 받는다.
#인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
def is_prime(prime_number):
    for i in range(2, prime_number):
        if prime_number % i == 0:
            return "소수 아님"
    return "소수"

result = is_prime(2)
print(result)     #소수
result = is_prime(13)
print(result)     #소수
result = is_prime(36)
print(result)     #소수 아님


#Quiz4-2
# [학생퀴즈] get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
# '고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
# '놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다.
def get_compliment(word):
    if '고구마' in word:
        return "왓쇼이!"
    elif '맛있는' in word:
        return "우마이!"
    elif '놀랄 만한' in word:
        return "요모야..!"
    elif '황당' in word:
        return "요모야..!"
    else:
        return "으무!"

result = get_compliment('고구마 피자')
print(result)  # 왓쇼이!
result = get_compliment('맛있는 밥')
print(result)  # 우마이!
result = get_compliment('황당하네')
print(result)  # 요모야..!
result = get_compliment('메롱')
print(result)  # 으무!


# Quiz5-1. 모듈이란?
# 필요한 것들이 부품처럼 정리된 파일
# Quiz5-2. 패키지란?
#모듈들을 모아놓은 집합
# Quiz5-3. theater_module.py 모듈(파일)의 price 함수를 p학번 라는 이름으로 호출 하도록 import문을 작성하세요
# class package:
#     def detail(self):
#         print("학번")
#
# import travel.thiland
# grade = travel.thailand.package()
# grade.detail()
#
# Quiz5-4. __all__의 역할은?
# 패키지를 생성 및 사용할 때 사용
#
# Quiz5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?
# __all__
# Quiz5-6. travel 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 ThailandPackage 클래스를 생성하고 detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
# import travel.vietnam
# < 가 >
# import travel.thailand.ThailandPackage
# trip_to = travel.thailand.ThailandPackage()
# trip_to. detail()
# from travel import vietnam
# < 나 >
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel.vietnam import ThailandPackage
# < 다 >
# trip_to = ThailandPackge()
# trip_to.detail()


