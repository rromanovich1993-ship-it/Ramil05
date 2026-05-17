# фцнкции
# def message (name,car ):
#     print(f""" Привет всем .
#     я видел сегодня что вы приехали на {car}
#     с уважением,{name} """)
#
# message(car = "BMW", name = "Рамиль")
# def creat_user(user_rol, user_name = "da"):
#     if user_name == None:
#         print(f"Пользователь с именем {user_name} создан и его роль в ситеме: {user_rol}")
#     else:
#         print(f"Пользователь создан БЕЗ имени {user_name} и его роль {user_rol}")
# creat_user("ADMIN")
#
# def kvadrat(number):
#     print(f"квадрат числа равен:{number**2}")
# kvadrat(5453545)
def id_coonekrtion(func):
     def wrapper():
         print("Подключение к БД")
         func()
         print("Отключение от БД")
     return wrapper

@id_coonekrtion
def login_test():
    print("Пользователь авторизован в БД")
login_test()


