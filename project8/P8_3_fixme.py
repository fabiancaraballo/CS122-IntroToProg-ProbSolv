# P8_3_fixme.py

# Help - when I run this program it does work right.
# It does not find names like ashley in the names list
# 

def linear_search(who, names):
    ''' Return index of name or None if not found'''
    index = 0
    for person in names:
        if person == who:
            return index
        elif person != who and index == len(names)-1:
            return None
        index += 1
    return None    

names = ['jim', 'tom', 'ashley', 'amanda', 'brittany', 'megan']

hint = "Type Q or type a name to search for (such as jim): "
find_name = input(hint).lower()

while find_name != 'q':
    index = linear_search(find_name, names)
    print()
    if index == None:
        print(find_name, 'NOT found in names list')
    else:
        print(find_name, 'found at offset', index, 'in names list')
    print()
    find_name = input(hint).lower()