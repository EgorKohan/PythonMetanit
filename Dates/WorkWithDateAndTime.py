import datetime
from datetime import time
from datetime import timedelta

yesterday = datetime.date(2022, 9, 13)
print(yesterday)

today = datetime.date.today()
print(today)

print("{}.{}.{}".format(today.day, today.month, today.year))

current_time = time(16, 25)
print(current_time)

deadline = datetime.datetime(2022, 4, 19, 15)
print(deadline)

'''
%d: день месяца в виде числа

%m: порядковый номер месяца

%y: год в виде 2-х чисел

%Y: год в виде 4-х чисел

%H: час в 24-х часовом формате

%M: минута

%S: секунда
'''

str_date = "2022-4-12"
strptime = datetime.datetime.strptime(str_date, "%Y-%m-%d")
print(strptime)

# Formatting of dates and time

'''
%a: аббревиатура дня недели. Например, Wed - от слова Wednesday (по умолчанию используются английские наименования)

%A: день недели полностью, например, Wednesday

%b: аббревиатура названия месяца. Например, Oct (сокращение от October)

%B: название месяца полностью, например, October

%d: день месяца, дополненный нулем, например, 01

%m: номер месяца, дополненный нулем, например, 05

%y: год в виде 2-х чисел

%Y: год в виде 4-х чисел

%H: час в 24-х часовом формате, например, 13

%I: час в 12-ти часовом формате, например, 01

%M: минута

%S: секунда

%f: микросекунда

%p: указатель AM/PM

%c: дата и время, отформатированные под текущую локаль

%x: дата, отформатированная под текущую локаль

%X: время, форматированное под текущую локаль
'''

today = datetime.date.today()
strftime = today.strftime("%dth of %B %Y %p %I:%M:%S")
print(strftime)

three_hours = timedelta(hours=3)
print(three_hours)

today_datetime = datetime.datetime.today()

print(today_datetime + three_hours)