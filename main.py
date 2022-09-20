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
do = input("Что сделать? Введи номер: ")
if do == "1":
  
  print("""Я могу:
1-написать число от 1 до 10
2-написать число с твоими числами""")
  do2 = input("Что мне сделать? Введи номер: ")
  if do2 == "1":
    random = random.randint(1,10)
    print(random)
  if do2 == "2":
    rn1 = input("Первое число: ")
    rn2 = input("Второе число: ")
    random = random.randint(int(rn1),int(rn2))
    print(random) 
if do == "2":
  number1 = input("Введи 1 число: ")
  number2 = input("Введи 2 число: ")

  print( "Ответ:", int(number1) + int(number2))
if do == "3":
  number3 = input("Введи 1 число: ")
  number4 = input("Введи 2 число: ")
  
  print( "Ответ:", int(number3) - int(number4))
  