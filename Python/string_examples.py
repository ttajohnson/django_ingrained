cap_sentence = "this string is a sentence."
print(cap_sentence.capitalize())

title_sentence = "this string is a title."
print(title_sentence.title())

split_sentence = "this string will be split"
print(split_sentence.split())

comma_split = "this string, will be split at the comma"
print(comma_split.split(","))

i_split = "this string will be split at every letter i"
print(i_split.split("i"))

index_example = "Hello World!"
print(index_example[0], index_example[6], index_example[-1])
print(index_example[0:5])

first_name = "Tim"
last_name = "Johnson"
print(f"Hello, {first_name} {last_name}!")
