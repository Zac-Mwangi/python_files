# generate a list of numbers

# won't include 5
# for n in range(5):
#     # do something
#     print(n)


# # range from...to...steps 
# # default step is 1
# for n in range(3,20,4):
#     print(n)


# # using with lists
burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']

# for n in range(len(burgers)):
#     print(n,burgers[n])


for n in range(len(burgers)-1,-1,-1):
    # start for last , end with -1 , and step is -1
    print(n , burgers[n])

