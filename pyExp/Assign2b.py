from itertools import chain
my_list = [{'Bhanu' : 57, 'Osama' : 49},
          {'Harsh' : 10, 'Farhan' : 23, 'Anshuman' : 50}]
print("The original list is : " + str(my_list))
all_keys = set(chain.from_iterable(my_list))
result = [dict((key, sub.get(key, None)) for key in all_keys) for sub in my_list]
print("New dictionaries list : " + str(result))