# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.


# a = int(input ('введите число от 1 до 7 '))
# if a <= 5 and a >0:
#     print ('да')
# elif a <= 7 and a >5:
#     print ('нет')
# else:
#     print ('неверное число')
    

# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится). 
# Пример: - x=34; y=-30 -> 4 - x=2; y=4-> 1 - x=-34; y=-30 -> 3 

# x = int(input('введите x '))
# y = int(input('введите y '))

# if x>0 and y>0:
#     print ('1 плоскость')
# elif x<0 and y>0:
#     print ('2 плоскость')
# elif x<0 and y<0:
#     print ('3 плоскость')
# elif x>0 and y<0:
#     print ('4 плоскость')
# else:
#     print('неверное число')


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a


# def checkPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     return result


# statement = inputNumbers(3)

# if checkPredicate(statement) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")



