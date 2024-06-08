import dublicate as d
numbers =d.int_list_with_duplicates
num=d.remove_dublicates(numbers)

sec_low = min(n for n in num if n != min(num))
# print(low)
print(sec_low)