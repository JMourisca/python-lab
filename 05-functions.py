def some_function(a_list, an_int=2, a_string="Default string"):
    a_list.append(a_string)
    return a_list, an_int % 2, len(a_string)


var1, var2, var3 = some_function([1, 2, 3])
print(var1)
print(var2)
print(var3)

var1, var2, var3 = some_function(a_string="Another string", a_list=[1, 7], an_int=2)
print(var1)
#
var1, var2, var3 = some_function([1, 2, 3], 5)
print(var1)
print(var2)
print(var3)

var1, var2, var3 = some_function([1, 2, 3], 5, "And now for something completely different")
print(var1)
print(var2)
print(var3)
