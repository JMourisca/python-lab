commands = ["12",
"insert 0 5",
"insert 1 10",
"insert 0 6",
"print",
"remove 6",
"append 9",
"append 1",
"sort",
"print",
"pop",
"reverse",
"print"]

list = []

for commandStr in commands[1:]:
    command_arr = commandStr.split(" ")
    command = command_arr[0]

    if command == "insert":
        index = int(command_arr[1])
        value = int(command_arr[2])
        list.insert(index, value)
    elif command == "print":
        print(list)
    elif command == "remove":
        value = int(command_arr[1])
        list.remove(value)
    elif command == "append":
        value = int(command_arr[1])
        list.append(value)
    elif command == "sort":
        list.sort()
    elif command == "pop":
        list.pop()
    elif command == "reverse":
        list.reverse()