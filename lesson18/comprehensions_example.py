'''import copy
some_list = [1,2,3,4,5,[5,6,[8]]]
#other_list = []

#for item in some_list:
#    other_list.append(item)

other_list = copy.copy(some_list)
print(other_list)
print(some_list)
other_list.append(5)
print(id(other_list[5][0]))
print(id(some_list[5][0]))
print(other_list)
print(some_list)
first_list = [1,2,3,4,5,[6,[6]]]
second_list = copy.deepcopy(first_list)
first_list[5][0] = 5
print(first_list)
print(second_list)

some_list = [1,2,3,4,5]
other_list = [item for item in some_list if item > 3]
print(other_list)



new_list = [item ** 2 for item in range(100)]
print(new_list)
print([print(item) for item in range(20)])

names = ['Alex', 'July', 'Matt']
new_dict_with_names = {index:name for index, name in enumerate(names)}
print(new_dict_with_names)

new_set = {item for item in [1,2,3,4,5,6,7,7,8] if item > 2}
print(new_set)'''
new_gen = (*(item for item in range(100)),)
print(new_gen)