'''
Циклы позволяют выполнять некоторое действие в зависимости от соблюдения некоторого условия. В языке Python есть следующие типы циклов:

while

for

https://metanit.com/python/tutorial/2.7.php

'''

number = 1

while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")

print("---")

'''
for переменная in набор_значений:
    инструкции
'''

message = "Hello"
for c in message:
    print(c)
else:
    print("End of message")

print("---")

number = 0
while number < 5:
    number += 1
    if number == 3 :    # если number = 3, переходим к новой итерации цикла
        continue # or break
    print(f"number = {number}")