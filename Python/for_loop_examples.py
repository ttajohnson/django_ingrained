my_iterable = [1, 2, 3]

for item_name in my_iterable:
    print(item_name)

mylist = [1, 2, 3, 4, 5]

for item in mylist:
    print("Hello")

for item in mylist:
    print(f"Example: {item}")

tuple_list = (1, 2, 3, 4, 5)

for tuple_item in tuple_list:
    print(tuple_item)

employees = {"ceo": "cindy", "cfo": "james"}

for key in employees:
    print(key)

for position in employees:
    print(f"Position: {position} - Employee: {employees[position]}")

tuple_unpack_list = [("a", "b"), ("c", "d"), (1, 2)]

for unpacked in tuple_unpack_list:
    print(unpacked)

for item1, item2 in tuple_unpack_list:
    print(item1)
    print(item2)
    print("hello")
