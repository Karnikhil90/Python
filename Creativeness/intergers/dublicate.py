
""" The variables contain 30 numbers or strings"""
int_list_with_duplicates = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20
]

names_with_duplicates = [
    "Alice", "Bob", "Charlie", "Diana", "Emma", "Frank", "Grace", "Harry", "Ivy", "Jack",
    "Alice", "Bob", "Charlie", "Diana", "Emma", "Frank", "Grace", "Harry", "Ivy", "Jack",
    "Alice", "Bob", "Charlie", "Diana", "Emma", "Frank", "Grace", "Harry", "Ivy", "Jack"
]

def remove_dublicates(numbers:list)->list:
    return [num for num in {key:None for key in numbers}]

# print(remove_dublicates(int_list_with_duplicates))
# print("="*30)
# print(remove_dublicates(names_with_duplicates))