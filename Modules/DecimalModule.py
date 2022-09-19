from decimal import Decimal

number = 0.1
print(number + number + number)

number = Decimal("0.1")
print(number + number + number)

# https://metanit.com/python/tutorial/6.4.php

number = Decimal("0.444")
number = number.quantize(Decimal("1.00"))
print(number)

number = Decimal("0.555678")
number = number.quantize(Decimal("1.00"))
print(number)