import collections
my_list = [[(26,6)], [(56)], [(6)],[(26,6)] ]
print("Given list is:\n", my_list)
result = collections.defaultdict(int)
for i in my_list:
    result[i[0]] += 1
print("Count of tuples present in the list:\n",result)
def removeDuplicates(my_list):
    return [t for t in (set(tuple(i) for i in my_list))]
print("New list after removing duplicates:",removeDuplicates(my_list))