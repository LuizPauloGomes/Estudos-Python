print('==== Conversor de temperatura ====')
tempcel = float(input('Qual a temperatura em graus °C: '))
kelvin = tempcel + 273.15
fahrenheit = (tempcel * (9 / 5)) + 32
print('{:.2f}°C corresponde á {:.2f}K'.format(tempcel, kelvin))
print('{:.2f}°C corresponde á {:.2f}°F'.format(tempcel, fahrenheit))
