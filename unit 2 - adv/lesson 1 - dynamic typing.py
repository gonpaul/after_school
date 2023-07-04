'''
import copy
#ways to copy data
input_list = [int(x) for x in input().split(',')]
copy1 = input_list[:]
copy2 = input_list.copy()
copy3 = copy.copy(input_list)
copy4 = copy.deepcopy(input_list)
copy5 = list(input_list)
'''
#4
import sys

animals = ['cat', 'cat', 'dog', 'dog', 'bird', 'capybara', 'capybara', 'capybara']
res_dict = {animals[i]: animals.count(animals[i]) for i in range(len(animals))}
values_dict = res_dict.values()
print(sum(values_dict), sum(sys.getrefcount(x) for x in range(1,4)))
#answer: 8 190

#5
backpack = ['capybara', 'capyraba', 'capyba', 'capyba', 'capybara', 2999, 2999, 'capybara',
            [7,7,7], [7,7,7], [7,7,7], [7,7,7]] + [[8,8]] * 5
count_equal = 0
count_same_object = 0
for x in range(len(backpack)-1):
    for y in range(x + 1, len(backpack)):
        if backpack[x] == backpack[y]:
            count_equal += 1
        if backpack[x] is backpack[y]:
            count_same_object += 1
print(count_same_object,count_equal)
#15 21

#6
import copy
the_caesar_salad = ['lettuce', 'chicken', 'cheese', 'sauce', 'tomatoes', 'croutons']
the_caesar_salad.append(the_caesar_salad)
b = copy.copy(the_caesar_salad)
the_caesar_salad += ['salt', 'pepper']
#print(the_caesar_salad[6] is b[6])
print(b[6][4], b[6][-1])
#tomatoes pepper
