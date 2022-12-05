def temp_celciusonv(celcius):
    fahren = round(celcius*9/5 +32)
    kelvin = round(celcius + 273.15)
    ret_list = [fahren, kelvin]
    if kelvin < 0:
        return 'invalid'
    else:
        print(ret_list)

temp_celciusonv(int(input('Enter Temperature in Celcius: ')))