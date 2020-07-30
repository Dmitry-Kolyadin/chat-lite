














def reg():
    login=input("")
    email=input("")
    fist_name=input("")
    last_name=input("")
    promo_kod=input("")
    password=input("")
    last_password=input("")
    kapcha=input("")
    name_devais=input("Введите имя этого устройства")

def login():
    login=input("")
    password=input("")
    while 1:
        new_devais_input=input("")
        if new_devais_input=="Да" or new_devais_input=="да" or new_devais_input=="ДА" or new_devais_input=="дА":
            new_devais=1
            break
        elif new_devais_input=="нет" or new_devais_input=="Нет" or new_devais_input=="НЕТ" or new_devais_input=="нЕТ":
            new_devais=0
            break
        else:
            print('Вы ввели некоректный ответ')
    if new_devais:
        name_devais=input("Введите имя этого устройства")
    else:
        pass


def akkyasorno():
    akk=input("У вас есть аккаунт? (да / нет)")
    if akk=="Да" or akk=="да" or akk=="ДА" or akk=="дА":
        login()
    elif akk=="нет" or akk=="Нет" or akk=="НЕТ" or akk=="нЕТ":
        reg()

akkyasorno()
