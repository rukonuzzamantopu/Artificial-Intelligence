my_dict = {'a': 10, 'b': 20, 'c': 15}
max_key = max(my_dict, key=my_dict.get)
print(f"The key with the maximum value in the dictionary {my_dict} is: '{max_key}' with a value of {my_dict[max_key]}.")
