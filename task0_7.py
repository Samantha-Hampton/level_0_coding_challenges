def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5 / 9
    return celcius


print(celcius_to_fahrenheit(34))
print(fahrenheit_to_celcius(34))
