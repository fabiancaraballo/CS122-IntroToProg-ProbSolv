def euros_to_dollars(euros):
    value = euros * 1.09
    return value

def dollars_to_euros(dollars):
    value = format(dollars / 1.09, '.2f')
    return value

dollars = euros_to_dollars(10)
print(dollars)

euros = dollars_to_euros(13)
print(euros)

def fahr_to_celsius(f_temp):
    value = f_temp // 180
    value = value * 100
    return value

def celsius_to_fahr(c_temp):
    value = c_temp // 100
    value = value * 180
    value = value + 32
    return value

fahr1 = 32
fahr2 = 212
celsius1 = 0
celsius2 = 100

print(fahr_to_celsius(fahr1))
print(fahr_to_celsius(fahr2))
print(celsius_to_fahr(celsius1))
print(celsius_to_fahr(celsius2))