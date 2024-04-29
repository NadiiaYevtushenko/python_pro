# 2. Типи даних
# цій лекції ми розглянемо основні типи даних в Python 3 та їх використання. Ви дізнаєтеся про числові типи (int, float, complex), рядкові дані (str), логічний тип (bool) та колекції, такі як списки, кортежі, множини та словники. Основні операції та приклади використання кожного типу даних допоможуть вам краще розібратися з їхнім використанням в програмуванні. Запрошуємо до ознайомлення!
# Корисні посилання:
# 1. [Документація Python](https://docs.python.org/3/)
# 2. [Real Python - Python Data Types](https://realpython.com/python-data-types/)
# 3. [GeeksforGeeks - Python Data Types](https://www.geeksforgeeks.org/python-data-types/)
# 4. [Python - Built-in Types](https://docs.python.org/3/library/stdtypes.html)
# 5. [W3Schools - Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)
#
# ###########################    Home work 2  ######################################3
#
#
# 1 Рядки (Strings):
# a)Напишіть функцію, яка приймає рядок і повертає його довжину.
# b) Створіть функцію, яка приймає два рядки і повертає об'єднаний рядок.
# 2 Числа (Int/float):
# a) Реалізуйте функцію, яка приймає число і повертає його квадрат.
# b) Створіть функцію, яка приймає два числа і повертає їхню суму.
# c) Створіть функцію яка приймає 2 числа типу int, виконує операцію ділення та повертає чілу частину і залишок.
# 3 Списки (Lists):
# a)Напишіть функцію для обчислення середнього значення списку чисел.
# b)Реалізуйте функцію, яка приймає два списки і повертає список, який містить спільні елементи обох списків.
# 4 Словники (Dictionaries):
# a) Створіть функцію, яка приймає словник і виводить всі ключі цього словника.
# b)Реалізуйте функцію, яка приймає два словники і повертає новий словник, який є об'єднанням обох словників.
# 5 Множини (Sets):
# a) Напишіть функцію, яка приймає дві множини і повертає їхнє об'єднання.
# b) Створіть функцію, яка перевіряє, чи є одна множина підмножиною іншої.
# 6 Умовні вирази та цикли:
# a) Реалізуйте функцію, яка приймає число і виводить "Парне", якщо число парне, і "Непарне", якщо непарне.
# b) Створіть функцію, яка приймає список чисел і повертає новий список, що містить тільки парні числа.
# Не забудьте, що кожна функція повинна мати Docstring та, за необхідності, коментарі по коду


# 1. a
# def string_len(string):                        # len() знаходження довжини рядка
#     """ Returns the length of a string """
#     length = len(string)
#     return length
# input_string = input("Print the text: ")                         # Приклад
# print("Length of a string:", string_len(input_string))
# 1. b
# def add_2_in_1_strings(string1, string2):                         # add приймає два рядки і повертає об'єднаний рядок.
#     """ Takes two strings and returns a concatenated string (string1 та string2) """
#     add_2_in_1_strings = string1 + string2
#     return add_2_in_1_strings
# input_string1 = input("Print the string1: ")                       # Приклад
# input_string2 = input("Print the string2: ")
# print("A concatenated string:", add_2_in_1_strings(input_string1, input_string2))
# 2.a
# def square_of_number(number):                                      # приймає число і повертає його квадрат.
#     """ Returns the square of the input number """
#     square = number ** 2
#     return square
# input_number = float(input("Write your number: "))                  # Приклад
# result = square_of_number(input_number)
# print("The square of the input number: ", result)
# 2.b
# def sum_2_numbers(number1, number2):                                 # приймає два числа і повертає їй суму
#     """ a function that takes two numbers and returns their sum. """
#     return number1 + number2
# input_number1 = int(input("Enter first number: "))                    #Приклад
# input_number2 = int(input("Enter second number: "))
# print("The result of the first and the second number: ", sum_2_numbers(input_number1, input_number2))
# 2.c
# def the_whole_part_and_the_remainder_after_division(number1, number2): # приймає 2 числа типу int, виконує операцію ділення та повертає чілу частину і залишок
#     """Takes 2 int numbers, performs a division operation, and returns the quotient and remainder"""
#     quotient = number1 // number2
#     remainder = number1 % number2
#     return quotient, remainder
# dividend = float(input("Put the number in dividend: "))                # Приклад
# divisor = float(input("Put the number in divisor: "))
# print("The whole part and the remainder after division: ", the_whole_part_and_the_remainder_after_division(dividend, divisor))

# 3.a
# def calculate_average(numbers):                                          # обчислення середнього значення списку чисел
#     """ The function to calculate the average value of a list of numbers. """
#     numbers = [int(x) for x in numbers.split()]                          # Розділяємо рядок на числа та перетворюємо їх у цілі числа
#     total = sum(numbers)                                                 # обчислюєм суму числ
#     len_for_list = len(numbers)                                          # довжина рядка
#     average = total / len_for_list                                       # Обчислюємо середнє значення
#     return average
# input_numbers = input("Put some numbers using '': ")                     # Приклад
# print("The average value of a list of numbers:", calculate_average(input_numbers))
# 3.b
# def common_elements(list1, list2):                                         # спільні елементи для двох списків
#     """It takes two lists and returns a list that contains the common elements of both lists"""
#     common_elements_for_2_lists = []                                      # спільний список
#     for item in list1:                                                    # для чисел в листі1
#         if item in list2 and item not in common_elements_for_2_lists:     # якщо елементи в списку2 і не в спільному списку
#             common_elements_for_2_lists.append(item)                      # добавити в спільний лист
#     return common_elements_for_2_lists                                    # повернути результат
#
# input_list1 = input("Put some numbers for list 1 using '': ")
# list1 = input_list1.split()                                               # рядок у список, розділяючи його за пробілами
# input_list2 = input("Put some numbers for list 2 using '': ")
# list2 = input_list1.split()                                               # рядок у список, розділяючи його за пробілами
# result = common_elements(list1, list2)
# print("Common in two lists: ", result)
# 4.a
# def print_keys(dictionary):                                                 #функція, яка приймає дві множини і повертає їхнє об'єднання.
#     """It displays all keys of this dictionary"""
#     for key in dictionary.keys():
#         print(key)
# my_dict_for_task_4_a = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}         # приклад
# print_keys(my_dict_for_task_4_a)                                            # результат
# 4.b
# def merge_2_dict(dict1, dict2):                             # приймає 2 словники і повертає новий словник, який є об'єднанням обох словників
#     """The function that takes two dictionaries and returns a new dictionary that is the union of both dictionaries"""
#     merged_dict = dict1.copy()                              # ств копію першого словника
#     merged_dict.update(dict2)                               # оновлюємо перший словник значенням другого
#     return merged_dict
# dict1 = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}                           # приклад
# dict2 = {'key5': 5, 'key6': 6, 'key7': 7, 'key8': 8}
# merge_2_dict = merge_2_dict(dict1, dict2)
# print("Here we got 2 dict: ", merge_2_dict)                                   # результат
# 5.a
# def union_of_sets(set1, set2):                              #  приймає дві множини і повертає їхнє об'єднання.
#     """Returns the union of two sets."""
#     return set1.union(set2)
# set1_input = input("Enter elements for set1 using '': ")   # приклад
# set2_input = input("Enter elements for set1 using '': ")   # приклад
# set1 = set(map(int, set1_input.split()))                   #перетворення введених рядків у множини
# set2 = set(map(int, set2_input.split()))                   #перетворення введених рядків у множини
# union_result = union_of_sets(set1, set2)                   # об'єднання
# print("Here is the result of union sets:", union_result)   # результат
# 5.b
# def is_subset_one_of_another(set1, set2):
#     """Checks if set1 is a subset of set2."""
#     return all(element in set2 for element in set1)
# set1 = {1, 2}                                             # приклад
# set2 = {1, 2, 3, 4, 5}                                    # приклад
# print("set1 is subset of set2:", is_subset_one_of_another(set1, set2))  # результат
# set3 = {6, 7}                                             # приклад
# set4 = {1, 2, 3, 4, 5}                                    # приклад
# print("set3 is subset of set4:", is_subset_one_of_another(set3, set4))  # результат
# 6.a
# def check_odd_even(num):
#     """Accepts a number and outputs "Even" if the number is even, and "Odd" if it is odd."""
#     if num % 2 == 0:              # якщо парне то на друк - Парне
#         print("Even")
#     elif num % 2 != 0:            # якщо непарне то на друк - непарне
#         print("Odd")
#
# input_num = int(input("Enter a number: "))    # введіть своє число для перевірки
# check_odd_even(input_num)                     # звірка
# print("Thank you!")                           # закінчення циклу
# 6.b
# def filter_even_from_odd(numbers):                                      # Функція, яка приймає список чисел і повертає новий список, що містить тільки парні числа
#     """A function that takes a list of numbers and returns a new list containing only even numbers"""
#     even_from_odd = [int(num) for num in numbers if int(num) % 2 == 0]  # перетворення на ціле число, звіряєм на парність
#     return even_from_odd                                                # результат тількі парні числа
# input_numbers = input("Enter numbers separated by a comma: ")           # ввод даних для прикладу
# input_numbers = input_numbers.split(",")                                #  розділення
# print("Here is all even numbers: ", filter_even_from_odd(input_numbers)) # результат