
def ispalindrom(
    recive_data:str
    ) -> bool:
    recive_data = recive_data.lower()
    revered = ""
    for i in recive_data:
        revered = i + revered
    if revered == recive_data:
        return True
    return False
# print(ispalindrom("mam"))

user_input_line = input("Enter the line : ")

line = user_input_line.split()

for i in range(len(line)):
    if ispalindrom(line[i]):
        print(line[i], end=" ")
