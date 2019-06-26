# P8_1_unending.py

# Help - when I run this program it keeps going and going...


my_list = ['Jim', 'Ashley', 'Amanda', 'Zelda']

# Add more names

hint = "Type Q to quit or first name to add (such as Anne): "
name = input(hint).title()
while name != 'Q':
    my_list.append(name)
    print("Added", name)
    name = input(hint).title()
