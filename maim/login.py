






# вход с нового устройства
def logining(data):
    pass

# вход с зарегистрированным устройством
def login_devise(data):
    pass

# создание аккаунта
def reg():
    login=input("Введите логин\n")
    email=input("\n")
    fist_name=input("\n")
    last_name=input("\n")
    promo_kod=input("\n")
    password=input("Введите пароль\n")
    last_password=input("Повторите пароль\n")
    kapcha=input("\n")
    name_devais=input("Введите имя этого устройства\n")

# вход в аккаунт
def login():
    login=input("Введите ваш логин\n")
    password=input("Введите ваш пароль\n")
    while 1:
        new_devais_input=input("Это новое устройство? (да / нет)\n")
        if new_devais_input=="Да" or new_devais_input=="да" or new_devais_input=="ДА" or new_devais_input=="дА":
            new_devais=1
            break
        elif new_devais_input=="нет" or new_devais_input=="Нет" or new_devais_input=="НЕТ" or new_devais_input=="нЕТ":
            new_devais=0
            break
        else:
            print('Вы ввели некоректный ответ')
    if new_devais:
        name_devais=input("Введите имя этого устройства\n")
        data={
            'new_akkaynt':0,
            'login':login,
            'password':password,
            'new_devais':new_devais,
            'name_devais':name_devais,
            }
        print(data)
        logining(data)

    # вход с зарегистрированным устройсвом
    else:
        data={
            'new_akkaynt':0,
            'login':login,
            'password':password,
            'new_devais':new_devais,
            }
        print(data)
        login_devise(data)

#выбор регистрация/вход
def akkyasorno():
    while 1:
        akk=input("У вас есть аккаунт? (да / нет)\n")
        if akk=="Да" or akk=="да" or akk=="ДА" or akk=="дА":
            login()
            break
        elif akk=="нет" or akk=="Нет" or akk=="НЕТ" or akk=="нЕТ":
            reg()
            break
        else:
            print('Вы ввели некоректный ответ')


akkyasorno()
