# {"key1" : "value1", "key2" : "value2"}

employees = {"chef": "Amy", "ceo": "Meghan"}
print(employees["ceo"])

employees["waiter"] = "Michael"
print(employees)

employees["chef"] = "Allison"
print(employees["chef"])

print(employees["waiter"].upper())

###

stockies = {"GOGGL": [200, 210, 220], "GEM": [300, 200, 50]}
print(stockies["GOGGL"])

goggle_history = stockies["GOGGL"]
print(f"First day Goggle price is: {goggle_history[0]}")

###

nest_dicts = {"outer": {"inner": 100}}
print(nest_dicts["outer"])
print(nest_dicts["outer"]["inner"])

###

my_dict = {"key1": 100, "key2": 200, "key3": 400}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
