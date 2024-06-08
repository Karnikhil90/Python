lst_name = ["NIKHIL","KARMAKAR",34.12,"SCHOOL",False,"APEX",
            "AQUA",True,"BUS",0.13,"TRAIN","BOTTOL","PHONE","APPLE",1,True]

lst = [i.lower() if type(i)==str else "CONVERT="+str(i) for i in lst_name]
print('\n'.join(lst))