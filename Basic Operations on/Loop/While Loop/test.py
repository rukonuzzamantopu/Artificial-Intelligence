i=1
while i<5:
    print(i)
    i+=1

# Output:1 2 3 4

#------------------
i =1
while i<5:
    print(i)
    if i ==3:
        break
    i+=1

# Output:1 2 3

#------------------
i =0
while i<5:
    i+=1
    if i == 2:
        continue
    print(i)
# Output:1 3 4 5

#------------------

i =1
while i<5:
    print (i)
    i += 1
else:
    print("i is no longer less than 5")

#output:1 2 3 4 i is no longer less than 5
