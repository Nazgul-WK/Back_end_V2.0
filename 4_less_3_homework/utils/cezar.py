

alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# Создаем алфавит
smeshenie = int(input('Шаг шифровки: '))    #Создаем переменную с шагом шифровки
message = input("Сообщение для шифровки: ").upper()    #создаем переменнную, куда запишем наше сообщение
itog = ''    #создаем переменную для вывода итогового сообщения
for i in message:
    mesto = alfavit.find(i)    #Вычисляем места символов в списке
    new_mesto = mesto + smeshenie    #Сдвигаем символы на указанный в переменной smeshenie шаг
for i in message:
    mesto = alfavit.find(i)
    new_mesto = mesto + smeshenie
    if i in alfavit:
        itog += alfavit[new_mesto]  # Задаем значения в итог
    else:
        itog += i
print (itog)