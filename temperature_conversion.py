def c_to_f(celcius):
    fahrenheit = celcius * 9/5 + 32
    return fahrenheit


temp_c = float(input('Enter temperature in Celsius: '))
temp_f = c_to_f(temp_c)
print('Fahrenheit:', temp_f)
