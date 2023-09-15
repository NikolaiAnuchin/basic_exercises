# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names_repeat_number = {}
for student_name in students:
    if student_name['first_name'] not in names_repeat_number:
        names_repeat_number[student_name['first_name']] = 1
    else:
        names_repeat_number[student_name['first_name']] += 1

for name in names_repeat_number:
    print(name + ':', names_repeat_number[name])

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names_repeat_number = {}
for student_name in students:
    if student_name['first_name'] not in names_repeat_number:
        names_repeat_number[student_name['first_name']] = 1
    else:
        names_repeat_number[student_name['first_name']] += 1

max_repeat_number = 0
for name in names_repeat_number:
    if max(max_repeat_number , names_repeat_number[name]) == names_repeat_number[name] :
        max_repeat_number = names_repeat_number[name]
        max_repeat_name = name
print("Самое частое имя среди учеников:", max_repeat_name)
    
# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
i = 0
for students in school_students:
    i += 1
    names_repeat_number = {}
    for student_name in students:
        if student_name['first_name'] not in names_repeat_number:
            names_repeat_number[student_name['first_name']] = 1
        else:
            names_repeat_number[student_name['first_name']] += 1

    max_repeat_number = 0
    for name in names_repeat_number:
        if max(max_repeat_number , names_repeat_number[name]) == names_repeat_number[name] :
            max_repeat_number = names_repeat_number[name]
            max_repeat_name = name
    print("Самое частое имя в классе", str(i) + ":" , max_repeat_name)

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for class_info in school:
    
    total_boys = 0
    total_girls = 0

    for student in class_info['students']:
        if is_male[student['first_name']]  is True:
            total_boys += 1
        else:
            total_girls += 1
    print("Класс", class_info['class'] + ":", "девочки", total_girls, "мальчики", total_boys )

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
max_boys = 0
max_girls = 0

for class_info in school:    

    total_boys = 0
    total_girls = 0

    for student in class_info['students']:
        if is_male[student['first_name']]  is True:
            total_boys += 1
        else:
            total_girls += 1

    if max(max_boys, total_boys) == total_boys:
        max_boys = total_boys
        max_boys_class = class_info['class'] 
    if max(max_girls, total_girls) == total_girls:
        max_girls = total_girls
        max_girls_class = class_info['class']     

print("Больше всего девочек в классе", max_girls_class, "\nБольше всего мальчиков в классе", max_boys_class)
