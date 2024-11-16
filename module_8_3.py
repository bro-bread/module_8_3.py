

class IncorrectVinNumber(Exception):
    """Исключение для неверного VIN-номера"""

    def __init__(self, message="Некорректный VIN-номер"):
        self.message = message
    def __str__(self):
        return self.message

class IncorrectCarNumbers(Exception):
    """Исключение для неверных номеров автомобиля"""

    def __init__(self, message="Некорректные регистрационные номера автомобиля"):
        self.message = message
    def __str__(self):
        return self.message

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int):
            if vin_number <= 999999 or vin_number >=  10000000:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
            else:
                return True
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers,  str):
            if len(numbers) == 6:
                return True
            else:
                raise IncorrectCarNumbers('Неверная длина номера')
        else:
            raise  IncorrectCarNumbers('Некорректный тип данных для номеров')



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')