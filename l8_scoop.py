# global scope
my_name = 'ryu'

def print_name():
    # overide local scope
    # my_name = "yoshi"
    # to overide global scope
    global my_name
    my_name = 'Yosho'
    print('Inside name is',my_name)


print_name()
print('outside name is',my_name)