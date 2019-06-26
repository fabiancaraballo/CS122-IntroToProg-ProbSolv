# P8_2_oops.py

# Help - when I run this program it does not work right.
# I cannot find names like amanda that are in the list
# 

def search(who, names):
    ''' Return index of name or None if not found'''
    index = 0
    for person in names:
        if person == who:
            return index
        elif person != who and index == len(names)-1:
            return None
        else:
            index+=1
   

my_list = ['jim', 'ashley', 'amanda', 'zelda', 'brittany']
my_gpa =  [3.05, 4.01,      2.87,      4.20,    1.95]


hint = "Type Q or type a name to search for (such as Jim): "
find_me = input(hint).lower()

while find_me != 'q':
    index = search(find_me, my_list)
    if index == None:
        print(find_me, 'NOT found in names list')
    else:
        print(find_me, 'found at offset', index, 'in names list')
        print(find_me, 'has a', my_gpa[index], 'grade point average')
    find_me = input(hint).lower()
        