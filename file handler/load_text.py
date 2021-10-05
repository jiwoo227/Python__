
print('한꺼번에 전체 읽기')
f = open('text.txt', 'r', encoding='utf-8')
data = f.read()
print(data)

print('한 줄씩 일기')

with open('text.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()  #line: 'hello\n'
        if line == '':   # 파일에서 익어올 내용 없으면 끝
            break
        print(line.rstrip()) #print('hello')


print('한꺼번에 전체 읽어서, 한줄씩 리스트')
with open('text.txt', 'r', encoding='utf-8')as f:
    lines = f.readlines()
    print(lines)
for line in lines:
    print(line)