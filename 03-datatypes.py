sample = [1, ["another", "list"], ("a", "tuple")]
mylist = ["List item 1", 2, 3.14, 34, 5, 10, 9]
mylist[0] = "List item 1 again"  # We're changing the item.
# print(mylist)
# mylist[-1] = 3.21  # Here, we refer to the last item.
# print(mylist[:])
# print(mylist[:2])
# print(mylist[3:5])
# print(mylist[4:])

mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14}
mydict["pi"] = "sweet"  # This is how you change dictionary values.
# print(mydict)
# print(mydict)
# print(mydict[2])
#
mytuple = (1, 2, 3)
myfunction = len
print(myfunction(mytuple))  # equivalent to len(mylist)
#
print("This %(verb)s a %(noun)s." % {"noun": "test", "verb": "is"})
#
name = "Juliana"
print("Hello, {}!".format(name))
print(f"Hello, {name}! =]")
