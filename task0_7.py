def celcius_to_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return f


def fahrenheit_to_celcius(f):
    c = (f - 32) * 5 / 9
    return c


print(celcius_to_fahrenheit(34))
print(fahrenheit_to_celcius(34))
