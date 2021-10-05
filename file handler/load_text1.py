print('한꺼번에 전체 읽기')
f = open('text.txt', 'r', encoding='utf-8')
data = f.read()
f.close()
print(data)
with open('text.txt', 'r', encoding='utf-8') as f:
    data = f.read()
print(data)

print('한 줄씩 일기')

print('한꺼번에 전체 읽어서, 한줄씩 리스트')