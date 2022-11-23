# To create an empty set
b = set()
print(type(b))
# To add in sets using .add()
b.add(5)
b.add(4)
b.add((1,2,3,4))# we can add tupple in set
# b.add({2:4}) or b.add([2,3]) #cannot add list or dictionary to sets.
print(b)
# length of sets
print(len(b))
# removal of sets element
b.remove(4)
print(b)
# To remove any element from set at random
print(b.pop())