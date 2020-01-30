# Source:
# https://nbviewer.jupyter.org/github/gumption/Python_for_Data_Science/blob/master/Python_for_Data_Science_all.ipynb

# single_instance_str = 'p,k,f,n,f,n,f,c,n,w,e,?,k,y,w,n,p,w,o,e,w,v,d'

# print('A', 'B', 'C', 1, 2, 3)
# print('Instance 1:', single_instance_str)
#
# print('A', 'B')  # no end argument
# print('C')
# print('A', 'B', end='...\n')  # end includes '\n' --> output cursor advancees to next line
# print('C')
# print('A', 'B', end='.')  # end=' ' --> use a space rather than newline at the end of the line
# print('C')  # so that subsequent printed output will appear on same line
#
# print(single_instance_str)
# print(single_instance_str[-1])
# print(single_instance_str[-2])

attribute_names = ['class',
                   'cap-shape', 'cap-surface', 'cap-color',
                   'bruises?',
                   'odor',
                   'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
                   'stalk-shape', 'stalk-root',
                   'stalk-surface-above-ring', 'stalk-surface-below-ring',
                   'stalk-color-above-ring', 'stalk-color-below-ring',
                   'veil-type', 'veil-color',
                   'ring-number', 'ring-type',
                   'spore-print-color',
                   'population',
                   'habitat']
# print(attribute_names)

single_instance_str = 'p,k,f,n,f,n,f,c,n,w,e,?,k,y,w,n,p,w,o,e,w,v,d\n'
# print(single_instance_str)
# print(single_instance_str.split(','))
# first strip leading & trailing whitespace, then split on commas
single_instance_list = single_instance_str.strip().split(',')
# print(single_instance_list)
# print("/".join(single_instance_list))
#
# print(dir(single_instance_list))

# attribute = 'bruises'  # try substituting 'bruises?' for 'bruises' and re-running this code
#
# if attribute in attribute_names:
#     i = attribute_names.index(attribute)
#     print(attribute, 'is in position', i)
# else:
#     print(attribute, 'is not in [', ",".join(attribute_names[:4]), end=" ]...\n")


def attribute_value(f_instance, f_attribute, f_attribute_names):
    """Returns the value of attribute in instance, based on its position in attribute_names"""
    if f_attribute not in f_attribute_names:
        return None
    else:
        i = f_attribute_names.index(f_attribute)
        return f_instance[i]  # using the parameter name here


attribute = 'cap-shape'  # try substituting any of the other attribute names shown above
print(attribute, '=', attribute_value(single_instance_list, 'cap-shape', attribute_names))
