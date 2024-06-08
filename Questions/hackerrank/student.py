"""
    @date 08-06-2024
    Basically u have to print the second low marks of the student
    
    
"""



def find(array,key) -> int:
    index = []
    for i in range(len(array)):
        if array[i] == key:
            index.append(i)
    return index if len(index) != 0 else [-1]

if __name__ == '__main__':
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])

    # print(student)
    
    score = [score[-1] for score in student]
    second_low = min(n for n in score if n != min(score))
    
    # print(f"secon low ={second_low}")
    index = find(score,second_low)
        
    data = []
    for i in index:
        if(len(index)==1 and index[0] == -1):
            break
        data.insert(0,student[i][0])
        
    #output=>
    for name in data: print(name)
    
    # second way of displaying
    # print('\n'.join(data))
    