# [09-05-2024] : Just remove dublicate from the list 


dub = ["a", "b", "c", "d", "a","b", "c", "d", "c", "d", "a", "b", "a"]
lst = []

for i in dub:
    if i not in lst:
        lst.append(i)
        
print(lst)