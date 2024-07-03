from randomDancing import rollWithIt

theDieSideUp = 'die_side_0' + str(rollWithIt())

with open(theDieSideUp, 'r', encoding='utf-8') as file:
    for i in file:
        print(i, end='')

# print(theDieSideUp) ----> This last line is unnecessary.
