import locale

locale.setlocale(locale.LC_ALL, "de")

number = 12345.6789
print(number)
formatted = locale.format_string("%f", number)
print(formatted)

print(locale.getlocale())