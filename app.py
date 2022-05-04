import os
##while True:
##    x = input('Введите адрес сайта\n')
##    if x == "завершить":
##        break
##    os.system('start https://www.'+ x)
list = []
for adres , papka,file in os.walk("C:\\"):
    for i in file:
        f = os.path.join(adres , i)
        list.append(f)
r = open('C:\\Users\Павел\Desktop\python\ text.txt')
##    for i in list:
##        r.write(i + "\n")
for i in r:
    if "Go.py" in i :
        print(i)
r.close()