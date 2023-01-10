# try: Block of code to be attempted.
# except: Block of code that will execute if there is an error.
# finally: Final block of code that will execute regardless of an error.
# Syntax errors cannot be caught; i.e. print("hello)

try:
    print("Hello!")
except:
    print("Error!")

try:
    print("10" + 10)
except:
    print("Error!")

try:
    print("10" + 10)
except TypeError:
    print("Type error detected.")

try:
    with open("test.txt", "r") as file:
        print(file)
except IOError:
    print("IO Error")
except TypeError:
    print("Type error detected.")

try:
    print(10 + 10)
except IOError:
    print("IO Error")
except:
    print("Hey you got an error...")
else:
    print("Else Block ran")

try:
    print("10" + 10)
except IOError:
    print("IO Error")
except TypeError:
    print("Type error detected.")
finally:
    print("Finally runs, error or no error.")
