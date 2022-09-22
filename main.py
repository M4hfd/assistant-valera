import random
name_assistant = "Валера"
print("Меня зовут " + name_assistant +"!")
username = input("Введите ваше имя: ")
print("Привет " + username + "!")
age_user = input("Сколько тебе лет? " )
print("Через 10 лет тебе будет:",int(age_user) + 10 ,"лет")
rise = input("Какой у тебя рост? Например мой: 0.53 м. ")
print("Ого! Ты выше меня на",float(rise) - 0.53, "метра!")
print("Приятно познакомиться: " + username + ", " + age_user +" лет!" + " с ростом " + rise + " метра!")
print("""Я могу: 
1-написать рандомное число, 
2-решить простой пример со сложением, 
3-решить простой пример с вычитанием""")
choice = input("Что сделать? Введи номер: ")
if choice == "1":
      
    print("Я могу:")
    print("1-написать число от 1 до 10")
    print("2-написать число с твоими числами")
    random_choice = input("Что мне сделать? Введи номер: ")
    if random_choice == "1":
        random = random.randint(1,10)
        print(random)
    if random_choice == "2":
        first_random_number = input("Первое число: ")
        second_random_number = input("Второе число: ")
        random = random.randint(int(first_random_number),int(second_random_number))
        print(random) 
if choice == "2":
    summation_first_number = input("Введи 1 число: ")
    summation_second_number = input("Введи 2 число: ")

    print( "Ответ:", int(number1) + int(number2))
if choice == "3":
    subtract_first_number = input("Введи 1 число: ")
    subtract_second_number = input("Введи 2 число: ")
  
    print( "Ответ:", int(number3) - int(number4)) 