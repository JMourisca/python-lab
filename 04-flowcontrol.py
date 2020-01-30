print(range(10))

rangelist = list(range(0, 10, 2))
print(rangelist)
#
for number in range(20):
    # Check if number is one of
    # the numbers in the tuple.
    if number in (11, 12):  # (3, 4, 7, 9):
        # "Break" terminates a for without
        # executing the "else" clause.
        print(f"{number} is in the list")
        # break
    else:
        # "Continue" starts the next iteration
        # of the loop. It's rather useless here,
        # as it's the last statement of the loop.
        print(f"{number} is not in the list")
        continue
    print("After if")

print("After for")

i = 5
while i < 10:
    print(i)
    i += 1
