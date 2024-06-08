def find(array, key) -> int:
    index = []
    for i in range(len(array)):
        if array[i] == key:
            index.append(i)
    return index if len(index) != 0 else [-1]

if __name__ == '__main__':
    student = [['d', 34.0], ['ef', 56.0], ['rr', 32.0]]
    print(student)
    
    # Extracting scores
    scores = [score[-1] for score in student]
    
    # Finding the second lowest score
    sorted_scores = sorted(set(scores))
    second_lowest = sorted_scores[1] if len(sorted_scores) > 1 else None
    
    print(f"second low = {second_lowest}")
    
    # Finding the student(s) with the second lowest score
    data = [[name, score] for name, score in student if score == second_lowest]
    
    print(scores)
    print(f"low = {data}")
