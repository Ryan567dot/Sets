numbers = {1,2,3,4,5,6}

#No duplicate element

list = [1,2,2,2,3]
tuple = (1,2,2,2,2,2,2,3)
set = {1,2,2,2,3,3,3,4,4,5}

print(tuple)


my_set = (1,2,3,4,5)
new_set = (1,2,3,4,5,6)
dup_set = (1,2,2,2,3,3,4)

my_set.add(5)

#Remove, discard

my_set.discard(4)
print(my_set)