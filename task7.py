try:
    age = int(input("Введите свой возраст: "))
except ValueError:
    print("Возраст должен быть числом")
    exit()
    
login = input("Введите свой логин: ")
password = input("Введите свой пароль: ")

if age >= 18 and login == "admin" and password == "admin":
    print("Роль: Администратор, доступ разрешен")
elif age >= 18 and login == "user" and password == "12345":
    print("Роль: Пользователь, доступ разрешен")
else:
    print("Доступ запрещен")