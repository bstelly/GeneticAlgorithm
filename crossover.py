from random import randint
def cross(parent_one, parent_two, pivot):
    offspring_one = ""
    offspring_two = ""
    length = len(parent_one)

    for x in range(0, length):
        if x < pivot:
            offspring_one += parent_two[x]
        else:
            offspring_one += parent_one[x]
        if x >= pivot:
            offspring_two += parent_two[x]
        else:
            offspring_two += parent_one[x]
    return (offspring_one, offspring_two)
    
a = "111111"
b = "000000"
offsprings = cross(a, b, 3)
offsprings