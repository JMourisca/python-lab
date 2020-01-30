#########
# Lists # Mutable
#########
a = 1
b = a
b = 3  # b has a copy of the value of "a"
print(a, b)

#
list_1 = [1, 3, 6, 9, 4, 2, 3]
list_2 = list_1

print('list_1:\t', list_1)
print('list_2:\t', list_2)
print()
#
list_1.remove(1)

print('list_1:\t', list_1)
print('list_2:\t', list_2)
print()
#
list_2.append(6)
print('list_1:\t', list_1)
print('list_2:\t', list_2)
print()
#
list_1.sort()
print('list_1:\t', list_1)
print('list_2:\t', list_2)
print()

list_3 = list_1[:]
list_3.append(5)
print('list_1:\t', list_1)
print('list_2:\t', list_2)
print('list_3:\t', list_3)
print(id(list_1))
print(id(list_2))
print(id(list_3))
print()
#
# list_1.append(10)
# print('list_1:\t', list_1)
# print('list_2:\t', list_2)
# print('list_3:\t', list_3)
# print()
#
# ##########
# # Tuples # Immutable
# ##########
# tuple_1 = (23, 3, 5, 21, 1, 9)
# tuple_2 = tuple_1
# print(tuple_1)
# print(tuple_2)
# print()
#
# tuple_1 = tuple_1.__add__((20, 12))
# print(tuple_1)
# print(tuple_2)
# print()
#
# print(tuple_1[1])
# print(list_1[1])
# print()
#
# list_1[2] = 666
# # tuple_1[2] = 666  # Doesn't work
# print(list_1)
