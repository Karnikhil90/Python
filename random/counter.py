lst = ["a", "b", "c", "d", "a","b", "c", "d", "c", "d", "a", "b", "a"]

ls1 =[]

for i in lst:
    c = 0
    for w in range(len(lst)):
        if(i == lst[w]):    c += 1
    print(f"'{i} found time = {c}'")