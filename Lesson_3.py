# 3. Вступ до ООП
# 1. **Python Official Documentation:**
#   - [Python 3 Documentation - Classes](https://docs.python.org/3/tutorial/classes.html)
#   - [Python 3 Documentation - Object-Oriented Programming](https://docs.python.org/3/tutorial/classes.html)
# 2. **Real Python:**
#   - [Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)
#   - [Inheritance and Composition: A Python OOP Guide](https://realpython.com/inheritance-composition-python/)
# 3. **GeeksforGeeks:**
#   - [Python - Object-Oriented Programming](https://www.geeksforgeeks.org/object-oriented-programming-in-python-set-1-class-and-its-members/)
#   - [Python - Inheritance](https://www.geeksforgeeks.org/inheritance-in-python/)
# 4. **W3Schools:**
#   - [Python Classes and Objects](https://www.w3schools.com/python/python_classes.asp)
#   - [Python Inheritance](https://www.w3schools.com/python/python_inheritance.asp)

# Необхідно написати класс Car який має атрибути fuel(паливо, задається за допомогою random.randrange(0, 9)),
# trip_distance(Відстань яку проїхав автомобіль), model (модель авто) та color(колір)ю реалізувати в класі
# метод move який приймає distance як аргумент.
# Створити 3 екземпляра цього классу
# В циклі while race_dist < desired_dist: необхідно для кожного екземпляру класу викликати метод move та
# передати йому значення random.randrange(0, 9). Метод move повинен додавати до trip_distance значення,
# яке було повернуто методом randomrange та зменшити кількість палива на це ж значення
# Як тільки один із автомобілів проїхав відстань більшу або яка дорівнює desired_dist - вивести
# повідомлення про те що автомобіль переміг, вказавши марку та дистанцію яку проїхав цей автомобіль.
# Цикл необхідно у такому випадку перервати
# Після циклу необхідно вивести повідомлення про те скільки і який автомобіль проїхав, та який
# у нього запас палива
# Домашку можна здати після терміну