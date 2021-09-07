import math
print(math.ceil(3.5))   # 천장 올림
print(math.ceil(3.4))
print(math.floor(3.5))  # 층 내림
print(math.floor(3.4))
print(round(3.5))
print(round(3.4))
print(math.pow(2,15))
print(math.sin(math.pi/2))

import random
print(random.random()) # 0.0 <= r < 1.0
print(random.randrange(1,10)) # 1<= r < 10정수
print(random.randint(1.10)) # 1<=r <= 10 정수
list1 = ['김치찌개', '비빔면', '안먹고 잠']
print(random.choice(list1))
print('before:', list1)
random.shuffle(list1)
print('after:' , list1)

print(random.sample(list1,2))

import datetime
print('-' * 20)
now = datetime.datetime.now()
print(now)
birthday = datetime.datetime(2004, 1, 5, 14, 0)
print(birthday)
print(now - birthday)