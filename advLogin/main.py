from FileAccess import FileAccess

FlAc= FileAccess('advLogin\\userdata.json')
userData=FlAc.read_data()

"""This list which contain Dictionaries(key: name, password) 
 and i have to transfer into 2 list(name,password)"""

name = []
password = []
for data in userData:
  name.append(data['name'])
  password.append(data['password'])
  
# ! Debug: cheak the data 
# ?print('Name=', name)
# ?print('Password=', password)

# TODO: Basic Login
print('1.login \n2. create a new user') 
choice =input("Enter your choice :")
if choice == '1':
    if input("Tell me ur name : ") in name:
        if input("Enter your password: ") in password:
            print("Login Successfully")
        else:
            print("Password is incorrect")
    else:
        print("User did not exist")
elif choice == '2':
    print("Create a new user id :")
    new_entry = {"name": input("Name: "), "password": input("Pass: ")}
    FlAc.add_data(new_entry)
    print("ID has been created successfully")
elif choice.lower() == 'show':
    print('Name=', name)
    print('Password=', password)
else:
    print("Give a vaild choice")