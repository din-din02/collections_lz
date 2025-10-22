slovar= {'Karina': 'Street 24', 'Natasha': 'Sorokino 7', 'Dasha': 'London 12'}   #our dict
n = 0                                                              #переменная для операций 
print('Словарь: ', slovar)
while n != 4:                                                  #цикл операций
    #выбор операций
    n = int(input('1-Удалить запись, 2-Изменить адресс, 3-Посмотреть словарь: '))
    match n:
         case 1:        #1 операция
            a = str(input('Кого хотите удалить? ')) #имя удаляемого
            if a in slovar:  #проверка нахождения элемента
                del slovar[a]
            else:
                print('Ошибка: такого человека и так нет в базе')

        #2 операция
         case 2:
        #имя изменяемого
            b = str(input('Кого адресс хотите изменить? '))
        #его новый адресс
            c = str(input('Какой его новый адресс? '))

        #проверка нахождения элемента
            if b in slovar:
                slovar[b] = c
            else:
                print('Error: такой человек не найден')

        #операция 3
         case 3:
             print('Адресса: ', slovar)
         case 4:
             n=4
        
