#!/usr/bin/pyth0n3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        number = my_list[idx]
        print(number)


list = [1, 2, 3]
element_at(list, 1)
