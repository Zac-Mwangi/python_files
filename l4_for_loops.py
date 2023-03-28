ninjas = ['ryu', 'crystal', 'yoshi', 'ken']

# for ninja in ninjas:
#     print(ninja)


# loop through a section
# for ninja in ninjas[1:3]:
#     print(ninja)


for ninja in ninjas:
    if ninja == "yoshi":
        print(f'{ninja} - black belt')
        # break out of the loop
        break
    else:
        print(ninja)
