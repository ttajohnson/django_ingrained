def name_of_function(name):
    """
    Docstring to explain function.
    """
    print("Hello " + name)


name_of_function("Tim")


def add_function(num1, num2):
    return num1 + num2


result = add_function(1, 2)

print(result)


def say_hello(first_name, last_name):
    return f"Hello {first_name} {last_name}"


greeting = say_hello(first_name="Tim", last_name="Johnson")

print(greeting)


def checker(num):
    if num >= 100:
        return "Greater than 100!"
    else:
        return "Not greater than 100..."


print(checker(99))
print(checker(110))

mylist = [1, 2, 3, 4, 7, 2, 8, 4, 8, 10, 6, 2, 51]
my_otherlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def check_list(list_to_check):
    for num in list_to_check:
        if num == 10:
            return True
    return False


print(check_list(mylist))
print(check_list(my_otherlist))
