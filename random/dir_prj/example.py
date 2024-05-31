from main import list_files
file_list = list_files("./images")
# print('\n'.join([name for name in list(filter(lambda name,i: name[-4:] == ".ico" i+=1, file_list))]))
# print('\n'.join([name for name in file_list]))
# print(file_list)

def fileCounter(fileList:list=[], fileExtention:str = ".jpg") -> int:
    fileExtention = ".jpg" if fileExtention == "" else fileExtention 
    if fileExtention in [".jpg", ".png", ".ico"]:
        counter = -1 
        for name in fileList:
            if name[-4:] == fileExtention:
                counter+=1
        return counter if counter == -1 else counter + 1
    return -2
print(fileCounter(file_list,input("Tell the file extension")))