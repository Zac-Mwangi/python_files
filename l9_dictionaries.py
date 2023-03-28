# key value pairs
# looks like json

ninja_belt = {
    "cystal":"red belt",
    "ryu":"black belt",
}

# ACCESSINGTHE WHOLE DICTIONARY
# print (ninja_belt)

# # ACCESSING A VALUE WITH A KEY
# print (ninja_belt["cystal"])
# print (ninja_belt["ryu"])

# ACCESSING KEYS
# print('yoshi' in ninja_belt)
# print('ryu' in ninja_belt)

# PRINTING KEYS
# print(ninja_belt.keys())
# # type casting
# print(list(ninja_belt.keys()))

# # PRINTING VALUES
# print(ninja_belt.values())
# # type casting
# print(list(ninja_belt.values()))

# STORING IN VARIABLES
# vals = list(ninja_belt.values())
# # counting the number of instances
# print(vals.count('black belt'))

# ADDING NEW KEY VALUE PAIR
# ninja_belt['yoshi'] = 'blue belt'

# print(ninja_belt)



# ANOTHER WAY TO DEFINE A DICTIONARY
person = dict(name="Ayee" , age = 25, height = "6ft")
print(person)