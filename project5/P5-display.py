def nice_int(number, num):
    value = format(number, '7,d')
    return str(value)

hello = nice_int(1098, 7)
print(hello)

def nice_float(number, width, decimals):
    value = format(number, '12,.2f')
    return str(value)

float = nice_float(1098.189, 12, 2)
print(float)

def nice_left_str(string, width):
    show_str = string.ljust(width)
    return show_str

string = nice_left_str("Hello", 8)
print(string, ".")


