# 1. Написать функцию, которая возвращает true, если подаваемое на вход число является палиндромом, иначе false

# def palindrom(number):
#     number = str(number)
#     if len(number)%2 == 0:
#         for i in range(len(number)//2):
#             if number[0] == number[-1]:
#                 number = number[1:-1]
#             else:
#                 return "nope"
#     else:
#         while len(number) != 1:
#             if number[0] == number[-1]:
#                 number = number[1:-1]
#             else:
#                 return "nope"
#     return "yup"
# print(palindrom(123321))

# def palindrom(number):
#     number = str(number)
#     return "yup" if number == number[::-1] else "nope"
# print(palindrom(123321))


# 2. Написать функцию, которой на вход подается какая-то строка и разделитель и возвращает новую строку. Этот разделитель заменяет пробелы в строке. По умолчанию он - '.'

# def new_string(string, separator = '.'):
#     string = string.replace(' ', separator)
#     return string
# print(new_string("i am a gay dinosaur", "-"))

# string = "12.90"
# x1, y1 = string.split('.')
# print(x1, y1)


# 3. Написать функцию, которая возвращает значение расстояния между двумя точками. Каждая точка обозначается кортежем -> (x, y). Вторая точка может быть не указана, тогда считается, что она находиться в начале координат

# def cords_range(A, B = (0, 0)):
#     Ax, Ay = A[0], A[1]
#     Bx, By = B[0], B[1]
#     Ax, Ay, Bx, By = int(Ax), int(Ay), int(Bx), int(By)
#     high = Ay - By
#     wide = Ax - Bx
#     d = (high**2 + wide**2)**0.5
#     return d

# print(cords_range((2, 4), (5, 2)))


# 4. В функцию подаётся некоторое количество чисел и разделитель. Возвращается строка, в которой находятся эти числа, целочисленно поделенные на 10 и разделенные переданным разделителем, который по умолчанию должен быть равен '; '. Если переданное значение не является числом - игнорировать. То есть, в результирующей строке должны быть только числа, разделённые чем-то. Для этого используется функция isinstance

# def new_string(*array, separator = ';'):
#     new_str = []

#     for i in array:
#         if  isinstance(i, int) == True:
#             new_str.append(str(i//10))
    
#     return separator.join(new_str)

# print(new_string(10, 50, 4, 'gfg', 900))


# 6. Требуется написать любую простенькую функцию, в которой будет написан docstring. Также нужно этот docstring вывести.

# def function_name(parameters):
#     """this is foo"""
#     parameters += 1
#     return
# function_name(2)
# print(function_name.doc_)


# ___________________lambda функции
# 1. Написать функцию lambda, которая возводит число в квадрат. Применить функцию к каждому элементу в каком-нибудь списке, состоящему из чисел. 

# list_of_numbers = [12, 43, 67, 1, 2, 7, 76, 0]
# cube_function = lambda number: number ** 2
# new_list_of_numbers = list(map(lambda number: number ** 2, list_of_numbers))
# print(new_list_of_numbers)


# 4. Отфильтровать список так, чтобы в нём остались только числа, и только больше 10 с помощью lambda функций и filter

# garbage_list = [12, 6, 0, 1, True, "rawr", 65, "dnf", False, 78]
# only_numbers_list = list(filter(lambda var: isinstance(var, int), garbage_list))
# more_than_10_numbs_list = list(filter(lambda num: num > 10, only_numbers_list))
# print(more_than_10_numbs_list)