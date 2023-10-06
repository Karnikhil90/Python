# input block 
name = input("Enter your name : ")
name = name.lower()

# Store in a list for easy logic 
nameInList = name.split()
# remove the last name becaus its static
last_name = nameInList[len(nameInList)-1].capitalize()


new_name = ""
for i in nameInList[:-1]:
  new_name += i[0].upper() + "."

new_name += last_name
print(new_name)
