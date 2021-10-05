f = open('text.txt', 'r', encoding='uft-8')

data = f.read()

f.close()

print(data)