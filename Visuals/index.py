def login(name_Recived : str,
          pass_Recived : str
          ) -> bool:
    
    name = "1"
    passord = "1"
    if name == name_Recived:
        if passord == pass_Recived:
            return True
    else:
        return False