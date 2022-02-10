# converting from celsius to fahrenheit
def c_to_f(c):
    f = (c * 9 / 5) + 32
    return f


# converting from fahrenheit to celsius
def f_to_c(f):
    c = (f - 32) * 5 / 9
    return c


print(c_to_f(34))
print(f_to_c(34))
