#A R C – P I C S
numbers = [10, 0, -1, 7]
#names=['Amrata','Hrutuja','Sheetal']
#mix_list=['Amrata',24,'BCS']
print(numbers)          # [10, 0, -1, 7]

print(numbers[0])       # 10 (first element)

print(numbers.index(10))# 0 (index of value 10)

numbers.append(5)       # adds 5 at the end
print(numbers)          # [10, 0, -1, 7, 5]

numbers.extend([40,50]) # adds all elements from another list
print(numbers)          # [10, 0, -1, 7, 5, 40, 50]

numbers.insert(0, 20)   # inserts 20 at index 0
print(numbers)          # [20, 10, 0, -1, 7, 5, 40, 50]

numbers.remove(10)      # removes the first occurrence of 10
print(numbers)          # [20, 0, -1, 7, 5, 40, 50]

print(numbers.pop())    # removes and returns last element → 50
# list now: [20, 0, -1, 7, 5, 40]

print(numbers.count(20))# counts occurrences of 20 → 1

numbers.sort()          # sorts ascending
print(numbers)          # [-1, 0, 5, 7, 20, 40]

numbers.reverse()       # reverses order
print(numbers)          # [40, 20, 7, 5, 0, -1]

new_numbers = numbers.copy() # shallow copy
print(new_numbers)      # [40, 20, 7, 5, 0, -1]

numbers.clear()     #clear list
print(numbers)