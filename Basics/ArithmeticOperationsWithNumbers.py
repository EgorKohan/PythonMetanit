print(6 + 2)
print(6 - 2)
print(6 * 2)
print(6 / 2)
print(7 // 2)  # Целочисленное деление двух чисел: Данная операция возвращает целочисленный результат деления, отбрасывая дробную часть
print(6 ** 2)  # Возведение в степень:
print(7 % 2)

'''
Операции

Направление

**

Справо налево

* / // %

Слева направо

+ -

Слева направо

'''

number = 3 + 4 * 5 ** 2 + 7
print(number)

'''
+=

Присвоение результата сложения

-=

Присвоение результата вычитания

*=

Присвоение результата умножения

/=

Присвоение результата от деления

//=

Присвоение результата целочисленного деления

**=

Присвоение степени числа

%=

Присвоение остатка от деления
'''

firstNumber = 2.0001
secondNumber = 5
thirdNumber = firstNumber/5
print(thirdNumber)

print(round(thirdNumber))
print(round(thirdNumber, 5))

'''
Однако следует учитывать, что функция round() не идеальный инструмент. 
Например, выше при округление до целых чисел применяется правило, согласно которому, если округляемая часть 
одинаково удалена от двух значений, то округление производится до ближайшего четного значения.
В Python в связи с тем, что десятичная часть числа не может быть точно представлена в виде числа float, 
то это может приводить к некоторым не совсем ожидаемым результатам. 
Например:
'''

print(round(2.545, 2))  # 2.54
print(round(2.555, 2))  # 2.56 - округление до четного
print(round(2.565, 2))  # 2.56
print(round(2.575, 2))  # 2.58

print(round(2.655, 2))  # 2.65 - округление не до четного
print(round(2.665, 2))  # 2.67
print(round(2.675, 2))  # 2.67