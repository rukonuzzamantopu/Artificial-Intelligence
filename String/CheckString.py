txt = "The best things in life are free!"
print("free" in txt)
txt = "The best things in life are free!"
print("expensive" in txt)
txt = "The best things in life are free!"
print("free" not in txt)
txt = "The best things in life are free!"
print("expensive" not in txt)



#Use it in an if statement:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


""" To check if a certain phrase or character is NOT present in a string, we can use the keyword not in. """

txt = "The best things in life are free!"
print("expensive" not in txt)

""" print only if "expensive" is NOT present: """

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")