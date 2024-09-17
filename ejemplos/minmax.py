import random

def minmax(ls):
    if len(ls) == 0:
        return (None, None)
    else:
        result = (ls[0], ls[0])
        for i in list(range(1, len(ls))):
            if ls[i] < result[0]:
                result = (ls[i], result[1])
            if ls[i] > result[1]:
                result = (result[0], ls[i])
        return result

my_list = list(range(0, 1000))
random.shuffle(my_list)
print(my_list)
print(minmax(my_list))
