# agaricus-lepiota.data
# This data set includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the
# Agaricus and Lepiota Family (pp. 500-525 [The Audubon Society Field
# Guide to North American Mushrooms, 1981]). Each species is identified as definitely edible, definitely poisonous, or
# of unknown edibility and not recommended. This latter class was
# combined with the poisonous one. The Guide clearly states that there is no simple rule for determining the edibility
# of a mushroom; no rule like leaflets three, let it be'' for
# Poisonous Oak and Ivy.
#
# Number of Instances: 8124
#
# Number of Attributes: 22 (all nominally valued)
#
# Attribute Information: (classes: edible=e, poisonous=p)
#
# cap-shape: bell=b, conical=c, convex=x, flat=f, knobbed=k, sunken=s
# cap-surface: fibrous=f, grooves=g, scaly=y, smooth=s
# cap-color: brown=n ,buff=b, cinnamon=c, gray=g, green=r, pink=p, purple=u, red=e, white=w, yellow=y
# bruises?: bruises=t, no=f
# odor: almond=a, anise=l, creosote=c, fishy=y, foul=f, musty=m, none=n, pungent=p, spicy=s
# gill-attachment: attached=a, descending=d, free=f, notched=n
# gill-spacing: close=c, crowded=w, distant=d
# gill-size: broad=b, narrow=n
# gill-color: black=k, brown=n, buff=b, chocolate=h, gray=g, green=r, orange=o, pink=p, purple=u, red=e, white=w, yellow=y
# stalk-shape: enlarging=e, tapering=t
# stalk-root: bulbous=b, club=c, cup=u, equal=e, rhizomorphs=z, rooted=r, missing=?
# stalk-surface-above-ring: fibrous=f, scaly=y, silky=k, smooth=s
# stalk-surface-below-ring: fibrous=f, scaly=y, silky=k, smooth=s
# stalk-color-above-ring: brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y
# stalk-color-below-ring: brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y
# veil-type: partial=p, universal=u
# veil-color: brown=n, orange=o, white=w, yellow=y
# ring-number: none=n, one=o, two=t
# ring-type: cobwebby=c, evanescent=e, flaring=f, large=l, none=n, pendant=p, sheathing=s, zone=z
# spore-print-color: black=k, brown=n, buff=b, chocolate=h, green=r, orange=o, purple=u, white=w, yellow=y
# population: abundant=a, clustered=c, numerous=n, scattered=s, several=v, solitary=y
# habitat: grasses=g, leaves=l, meadows=m, paths=p, urban=u, waste=w, woods=d
# Missing Attribute Values: 2480 of them (denoted by "?"), all for attribute #11.
#
# Class Distribution: -- edible: 4208 (51.8%) -- poisonous: 3916 (48.2%) -- total: 8124 instances
import os
import math
from collections import Counter


def load_instances(filename):
    ai = []
    with open(filename, 'r') as f:
        for line in f:
            ai.append(line.strip().split(','))

    return ai


def load_attribute_names_and_values(filename):
    attribute_names_and_values = []
    with open(filename, 'r') as f:
        for line in f:
            attr_dict = {}
            data_split = line.strip().split(':')
            name = data_split[0]
            attr_dict['name'] = name
            values = data_split[1].strip().split(",")
            attr_dict['values'] = {}
            for v in values:
                vn = v.strip().split("=")
                attr_dict['values'][vn[1]] = vn[0]
            attribute_names_and_values.append(attr_dict)
    return attribute_names_and_values


def attribute_value_counts(instances, attribute_name, attr_names):
    value_counts = Counter()
    index = 0
    for attr in attr_names:
        if attr["name"] == attribute_name:
            break
        index += 1

    for inst in instances:
        value = inst[index]
        value_counts[value] += 1
    return value_counts


def print_all_attribute_value_counts(clean_inst, attr_names):
    total_instances = len(clean_instances)
    index = 0
    for an in attr_names:
        value_counts = Counter()
        attribute_name = an["name"]
        print(f'{attribute_name}:', end=" ")

        for inst in clean_inst:
            value = inst[index]
            value_counts[value] += 1

        for v in value_counts:
            val = value_counts[v]
            print('{} = {} ({:5.3f}),'.format(v, val, val/total_instances), end=" ")
        index += 1
        print()
    # print(f'{name}:')


def entropy(instances):
    counter = Counter()
    total = len(instances)
    for i in instances:
        counter[i[0]] += 1
    p1 = counter["e"] / total
    p2 = counter["p"] / total
    return -p1 * math.log2(p1) - p2 * math.log2(p2)


DELIMITER = "|"
UNKNOWN_VALUE = "?"

# attribute_names = ['class',
#                    'cap-shape', 'cap-surface', 'cap-color',
#                    'bruises?',
#                    'odor',
#                    'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
#                    'stalk-shape', 'stalk-root',
#                    'stalk-surface-above-ring', 'stalk-surface-below-ring',
#                    'stalk-color-above-ring', 'stalk-color-below-ring',
#                    'veil-type', 'veil-color',
#                    'ring-number', 'ring-type',
#                    'spore-print-color',
#                    'population',
#                    'habitat']

data_filename = 'agaricus-lepiota.data'
all_instances = load_instances(data_filename)

# Check if file was imported correctly
# print("Read", len(all_instances), "instances from", data_filename)
# print("First instance:", all_instances[0])
# print()

# print(f'Converting to {DELIMITER}-delimited strings, e.g.', DELIMITER.join(all_instances[0]))
# Generates new file with new delimiter
# datafile_2 = 'agaricus-lepiota-2.data'
# if os.path.exists(datafile_2):
#     os.remove(datafile_2)
#
# with open(datafile_2, 'w') as f:
#     for instance in all_instances:
#         f.write(DELIMITER.join(instance) + '\n')
#

# Gets attributes from attributes files
attribute_filename = 'agaricus-lepiota.attributes'
# delete 'simple_ml.' in the function call below to test your function
attribute_names_and_values = load_attribute_names_and_values(attribute_filename)
attribute_names = [x["name"] for x in attribute_names_and_values]
# print(attribute_names)

# print('Read', len(attribute_names_and_values), 'attribute values from', attribute_filename)
# print('First attribute name:', attribute_names_and_values[0]['name'], '; values:', attribute_names_and_values[0]['values'])

# Clear instances by removing those without all the informations, with ?
clean_instances = []
for instance in all_instances:
    if UNKNOWN_VALUE not in instance:
        clean_instances.append(instance)

# print(len(clean_instances), 'clean instances')

# Count edible
edible_count = 0
for instance in clean_instances:
    if instance[0] == 'e':
        edible_count += 1

# print('There are', edible_count, 'edible mushrooms among the', len(clean_instances), 'clean instances')

# Count cap state without counter
# cap_state_value_counts = {}
# for instance in clean_instances:
#     cap_state_value = instance[1]  # cap-state is the 2nd attribute
#     if cap_state_value not in cap_state_value_counts:
#         # first occurrence, must explicitly initialize counter for this cap_state_value
#         cap_state_value_counts[cap_state_value] = 0
#     cap_state_value_counts[cap_state_value] += 1

# print('Counts for each value of cap-state without counter:')
# for value in cap_state_value_counts:
#     print(value, ':', cap_state_value_counts[value])

# Count cap state with counter
# cap_state_value_counts = Counter()
# for instance in clean_instances:
#     cap_state_value = instance[1]
#     cap_state_value_counts[cap_state_value] += 1
#
# print('Counts for each value of cap-state with counter:')
# for value in cap_state_value_counts:
#     print(value, ':', cap_state_value_counts[value])
# print(cap_state_value_counts.most_common(3))

attribute = "cap-shape"
attribute_value_counts = attribute_value_counts(clean_instances, attribute, attribute_names_and_values)
# print('Counts for each value of', attribute, ':')

# for value in attribute_value_counts:
#     print(value, ':', attribute_value_counts[value])
# print()
#
# for value in sorted(attribute_value_counts):
#     print(value, ':', attribute_value_counts[value])
# print()
#
# for key, value in attribute_value_counts.items():
#     print(key, ":", value)
# print()

# print_all_attribute_value_counts(clean_instances, attribute_names_and_values)
print(entropy(clean_instances))
