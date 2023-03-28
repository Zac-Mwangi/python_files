# block of code that can be reused

# def greet():
#     print("Hello World!")

# greet()


# # passing parameters
# def greet(name, time):
#     print(f'Good {time} {name}, I hope you are well')

# greet("Shawn","Morning")


# # passing in parameters from users input
# def greet(name, time):
#     print(f'Good {time} {name}, I hope you are well')

# name = input('enter your name: ')
# time = input('enter time of the day: ')

# greet(name, time)


# # SETTING TO DEFAULT
# def greet(name = "Shawn", time = "Evening"):
#     print(f'Good {time} {name}, I hope you are well')

# # without passing any argument
# greet()
# # passing any argument
# greet(name = "David")
# # OR
# greet("David")



# AREA AND VOLUME

def area(radius):
    return(3.142 * radius * radius)

def vol(area, length):
    print(area * length)

radius = int(input('Enter a radius : '))
length = int(input('Enter a length : '))

# area_calc = area(radius)
# vol(area_calc, length)

# OR

vol(area(radius), length)
