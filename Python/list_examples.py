my_int = 4
a_list = [1, 2, 3, my_int]
print(a_list)

hundreds_list = [100, 200, 300, 400, 500]
print(hundreds_list[2])
print(hundreds_list[1:4:2])

hundreds_list.append(my_int)
print(hundreds_list)

hundreds_list.insert(0, my_int)
print(hundreds_list)

hundreds_list.pop()
print(hundreds_list)

tres_hundred = hundreds_list.pop(3)
print(hundreds_list)
print(tres_hundred)

hundreds_list.reverse()
print(hundreds_list)

hundreds_list.sort()
print(hundreds_list)
