# Comparison Operators
print(1 > 2)
print(1 < 2)
print(7 + 7 >= 10 + 4)
print(5 + 5 <= 9)
print(3 == 3)
print(3 == 4)
print(3 != 4)

record = "Tim"
match = "tim"
print(record == match)

record = "Johnson"
match = "Johnson"
print(record == match)

# Logical Operators
# and / or

print(1 > 2 and 2 == 2)
print(3 > 2 and 2 == 2)
print(2 < 1 or 3 == 3)

user_input = "mypassword"
stored_password = "mypassword"
print(user_input == stored_password)

###
# if / elif / else

if True:
    print("True!")
    print("Oh yeah!")

if False:
    print("False?")
    print("Oh no!")

if user_input == stored_password:
    print("It's a match!")

user_input = "tryyplassworb"
stored_password = "mypassword"
admin = True

if user_input == stored_password:
    print("It's a match!")
elif admin:
    print("Passwords don't match, but ADMIN priviledges granted!")
else:
    print("Not a match!")

user_input = "mypassword"
stored_password = "mypassword"
admin = True

if user_input == stored_password:
    print("It's a match!")
elif admin:
    print("Passwords don't match, but ADMIN priviledges granted!")
else:
    print("Not a match!")
